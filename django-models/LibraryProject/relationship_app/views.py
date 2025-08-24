from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Book, Library, Author, Librarian

# Function-based view to list all books
def list_books(request):
    """Function-based view that lists all books with their authors"""
    books = Book.objects.all().select_related('author')
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display library details
class LibraryDetailView(DetailView):
    """Class-based view that displays details for a specific library"""
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add librarian information to context
        try:
            context['librarian'] = self.object.librarian
        except Librarian.DoesNotExist:
            context['librarian'] = None
        return context

# Class-based view to list all libraries
class LibraryListView(ListView):
    """Class-based view that lists all libraries"""
    model = Library
    template_name = 'relationship_app/library_list.html'
    context_object_name = 'libraries'
    
    def get_queryset(self):
        return Library.objects.prefetch_related('books', 'books__author')

# Function-based view for the home page
def home(request):
    """Home page view with overview of the library system"""
    total_books = Book.objects.count()
    total_authors = Author.objects.count()
    total_libraries = Library.objects.count()
    total_librarians = Librarian.objects.count()
    
    context = {
        'total_books': total_books,
        'total_authors': total_authors,
        'total_libraries': total_libraries,
        'total_librarians': total_librarians,
        'recent_books': Book.objects.select_related('author').order_by('-id')[:5],
    }
    return render(request, 'relationship_app/home.html', context)