from django.urls import path
from .views import list_books, home, LibraryListView, LibraryDetailView

app_name = 'relationship_app'

urlpatterns = [
    # Home page
    path('', home, name='home'),
    
    # Function-based view for listing all books
    path('books/', list_books, name='list_books'),
    
    # Class-based views for libraries
    path('libraries/', LibraryListView.as_view(), name='library_list'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]