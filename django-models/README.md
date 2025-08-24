# Django Models - Complex Relationships

This project demonstrates complex relationships between Django models using ForeignKey, ManyToMany, and OneToOne fields.

## Project Structure

```
django-models/
├── LibraryProject/
│   ├── relationship_app/
│   │   ├── models.py          # Contains the model definitions
│   │   ├── query_samples.py   # Sample queries demonstrating relationships
│   │   ├── create_sample_data.py  # Script to populate database with sample data
│   │   ├── admin.py           # Django admin configuration
│   │   └── migrations/        # Database migrations
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

4. **Run the demonstration queries:**
   ```bash
   python relationship_app/query_samples.py
   ```

5. **Start the development server:**
   ```bash
   python manage.py runserver
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
2. **Reverse Relationships**: Accessing related objects from the "many" side
3. **QuerySet Methods**: filter(), get(), all(), count()
4. **Database Migrations**: Creating and applying model changes
5. **Django Admin Integration**: Managing models through the admin interface

## Sample Data

The project includes sample data with:
- **Authors**: J.K. Rowling, George R.R. Martin, Stephen King
- **Books**: Harry Potter series, A Game of Thrones, The Shining, It
- **Libraries**: Central Library, University Library
- **Librarians**: Sarah Johnson, Michael Brown

This demonstrates how the different relationship types work together in a real-world scenario.
