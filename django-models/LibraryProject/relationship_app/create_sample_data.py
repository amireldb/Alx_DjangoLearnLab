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
    print("Creating sample data...")
    
    # Create authors
    author1 = Author.objects.create(name="J.K. Rowling")
    author2 = Author.objects.create(name="George R.R. Martin")
    author3 = Author.objects.create(name="Stephen King")
    
    # Create books with publication years
    book1 = Book.objects.create(title="Harry Potter and the Philosopher's Stone", author=author1, publication_year=1997)
    book2 = Book.objects.create(title="Harry Potter and the Chamber of Secrets", author=author1, publication_year=1998)
    book3 = Book.objects.create(title="A Game of Thrones", author=author2, publication_year=1996)
    book4 = Book.objects.create(title="The Shining", author=author3, publication_year=1977)
    book5 = Book.objects.create(title="It", author=author3, publication_year=1986)
    
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
    print(f"Created {Author.objects.count()} authors")
    print(f"Created {Book.objects.count()} books")
    print(f"Created {Library.objects.count()} libraries")
    print(f"Created {Librarian.objects.count()} librarians")

if __name__ == "__main__":
    create_sample_data()
