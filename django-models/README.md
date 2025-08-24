# Django Models - Complex Relationships

This project demonstrates complex relationships between Django models using ForeignKey, ManyToMany, and OneToOne fields, along with a complete web interface showcasing both function-based and class-based views.

## Project Structure

```
django-models/
├── LibraryProject/
│   ├── relationship_app/
│   │   ├── models.py          # Contains the model definitions
│   │   ├── views.py           # Function-based and class-based views
│   │   ├── urls.py            # URL patterns for the app
│   │   ├── query_samples.py   # Sample queries demonstrating relationships
│   │   ├── create_sample_data.py  # Script to populate database with sample data
│   │   ├── admin.py           # Django admin configuration
│   │   └── migrations/        # Database migrations
│   ├── templates/
│   │   └── relationship_app/  # HTML templates for the web interface
│   │       ├── home.html      # Home page with overview
│   │       ├── list_books.html # Function-based view template
│   │       ├── library_list.html # Class-based ListView template
│   │       └── library_detail.html # Class-based DetailView template
│   ├── manage.py
│   └── LibraryProject/
│       ├── settings.py
│       └── urls.py
└── README.md
```

## Models Overview

### 1. Author Model
- **name**: CharField (max_length=50)
- Represents book authors

### 2. Book Model
- **title**: CharField (max_length=50)
- **author**: ForeignKey to Author (One-to-Many relationship)
- Represents books with their authors

### 3. Library Model
- **name**: CharField (max_length=50)
- **books**: ManyToManyField to Book (Many-to-Many relationship)
- Represents libraries that can contain multiple books

### 4. Librarian Model
- **name**: CharField (max_length=50)
- **library**: OneToOneField to Library (One-to-One relationship)
- Represents librarians assigned to specific libraries

## Relationship Types Demonstrated

1. **ForeignKey (One-to-Many)**: Book → Author
   - Each book has one author
   - Each author can have multiple books

2. **ManyToManyField (Many-to-Many)**: Library ↔ Book
   - Each library can have multiple books
   - Each book can be in multiple libraries

3. **OneToOneField (One-to-One)**: Librarian → Library
   - Each librarian is assigned to exactly one library
   - Each library has exactly one librarian

## Web Interface - Views Implementation

### Function-Based Views

1. **Home View** (`home`)
   - Displays overview statistics of the library system
   - Shows total counts of books, authors, libraries, and librarians
   - Lists recent books added to the system
   - Provides navigation links to other views

2. **List Books View** (`list_books`)
   - Function-based view that lists all books with their authors
   - Uses `select_related('author')` for efficient database queries
   - Renders a clean, styled list of all books in the system

### Class-Based Views

1. **Library List View** (`LibraryListView`)
   - Inherits from Django's `ListView`
   - Displays all libraries with book counts
   - Uses `prefetch_related('books', 'books__author')` for optimized queries
   - Provides links to individual library details

2. **Library Detail View** (`LibraryDetailView`)
   - Inherits from Django's `DetailView`
   - Shows detailed information about a specific library
   - Displays all books in the library with their authors
   - Shows the assigned librarian (if any)
   - Demonstrates OneToOne relationship access

## URL Patterns

```
relationship_app/
├── '' (home)                    # Home page with overview
├── 'books/' (list_books)        # Function-based view for all books
├── 'libraries/' (library_list)  # Class-based ListView for libraries
└── 'libraries/<int:pk>/'        # Class-based DetailView for specific library
```

## Setup Instructions

1. **Navigate to the project directory:**
   ```bash
   cd django-models/LibraryProject
   ```

2. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

3. **Create sample data (optional):**
   ```bash
   python relationship_app/create_sample_data.py
   ```

4. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

5. **Access the web interface:**
   - Home page: http://127.0.0.1:8000/relationship_app/
   - All books: http://127.0.0.1:8000/relationship_app/books/
   - Libraries: http://127.0.0.1:8000/relationship_app/libraries/
   - Admin panel: http://127.0.0.1:8000/admin/

6. **Run the demonstration queries:**
   ```bash
   python relationship_app/query_samples.py
   ```

## Sample Queries

The `query_samples.py` script demonstrates the following relationship queries:

### 1. Query all books by a specific author
```python
def query_all_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books
```

### 2. List all books in a library
```python
def list_all_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books
```

### 3. Retrieve the librarian for a library
```python
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    return librarian
```

## Template Features

### Home Page (`home.html`)
- Responsive design with CSS Grid
- Statistics cards showing system overview
- Navigation links to all major sections
- Recent books display

### Books List (`list_books.html`)
- Clean list display of all books
- Author information for each book
- Book count statistics
- Navigation between sections

### Library List (`library_list.html`)
- Hover effects for interactive experience
- Book count per library
- Links to individual library details
- Responsive design

### Library Detail (`library_detail.html`)
- Detailed library information
- Complete book list with authors
- Librarian information display
- Multiple navigation options

## Additional Relationship Examples

The script also demonstrates:
- Counting books per author using reverse relationships
- Counting books per library
- Accessing related objects through different relationship types

## Django Admin

All models are registered in the Django admin interface. You can access it at:
- URL: http://127.0.0.1:8000/admin/
- Create a superuser first: `python manage.py createsuperuser`

## Key Django Concepts Demonstrated

1. **Model Relationships**: ForeignKey, ManyToManyField, OneToOneField
2. **View Types**: Function-based views and Class-based views (ListView, DetailView)
3. **URL Patterns**: Named URL patterns with namespace
4. **Template System**: Django template language with filters and tags
5. **Database Optimization**: select_related() and prefetch_related()
6. **Reverse Relationships**: Accessing related objects from the "many" side
7. **QuerySet Methods**: filter(), get(), all(), count()
8. **Database Migrations**: Creating and applying model changes
9. **Django Admin Integration**: Managing models through the admin interface

## Sample Data

The project includes sample data with:
- **Authors**: J.K. Rowling, George R.R. Martin, Stephen King
- **Books**: Harry Potter series, A Game of Thrones, The Shining, It
- **Libraries**: Central Library, University Library
- **Librarians**: Sarah Johnson, Michael Brown

This demonstrates how the different relationship types work together in a real-world scenario with a complete web interface.
