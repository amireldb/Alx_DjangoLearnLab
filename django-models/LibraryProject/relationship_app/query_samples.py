import os
import sys
import django

# Add the project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def create_sample_data():
    """Create sample data for demonstration"""
    # Create authors
    author1 = Author.objects.create(name="J.K. Rowling")
    author2 = Author.objects.create(name="George R.R. Martin")
    author3 = Author.objects.create(name="Stephen King")
    
    # Create books
    book1 = Book.objects.create(title="Harry Potter and the Philosopher's Stone", author=author1)
    book2 = Book.objects.create(title="Harry Potter and the Chamber of Secrets", author=author1)
    book3 = Book.objects.create(title="A Game of Thrones", author=author2)
    book4 = Book.objects.create(title="The Shining", author=author3)
    book5 = Book.objects.create(title="It", author=author3)
    
    # Create libraries
    library1 = Library.objects.create(name="Central Library")
    library2 = Library.objects.create(name="University Library")
    
    # Add books to libraries
    library1.books.add(book1, book2, book3)
    library2.books.add(book3, book4, book5)
    
    # Create librarians
    librarian1 = Librarian.objects.create(name="Sarah Johnson", library=library1)
    librarian2 = Librarian.objects.create(name="Michael Brown", library=library2)
    
    print("Sample data created successfully!")

def query_all_books_by_author(author_name):
    """
    Query all books by a specific author
    """
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"\nBooks by {author_name}:")
        for book in books:
            print(f"- {book.title}")
        return books
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found.")
        return []

def list_all_books_in_library(library_name):
    """
    List all books in a library
    """
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"\nBooks in {library_name}:")
        for book in books:
            print(f"- {book.title} (by {book.author.name})")
        return books
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
        return []

def get_librarian_for_library(library_name):
    """
    Retrieve the librarian for a library
    """
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        print(f"\nLibrarian for {library_name}: {librarian.name}")
        return librarian
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
        return None
    except Librarian.DoesNotExist:
        print(f"No librarian found for {library_name}.")
        return None

def demonstrate_relationships():
    """
    Demonstrate all the relationship queries
    """
    print("=== Django Model Relationships Demonstration ===\n")
    
    # Query all books by a specific author
    query_all_books_by_author("J.K. Rowling")
    
    # List all books in a library
    list_all_books_in_library("Central Library")
    
    # Retrieve the librarian for a library
    get_librarian_for_library("Central Library")
    
    # Additional demonstrations
    print("\n=== Additional Relationship Examples ===")
    
    # Get all authors with their book counts
    authors = Author.objects.all()
    for author in authors:
        book_count = author.book_set.count()
        print(f"{author.name} has {book_count} book(s)")
    
    # Get all libraries with their book counts
    libraries = Library.objects.all()
    for library in libraries:
        book_count = library.books.count()
        print(f"{library.name} has {book_count} book(s)")

if __name__ == "__main__":
    # Uncomment the line below to create sample data (run only once)
    # create_sample_data()
    
    # Run the demonstration
    demonstrate_relationships()