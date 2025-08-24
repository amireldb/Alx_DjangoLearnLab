from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title} by {self.author.name}"
    
    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

class Library(models.Model):
    name = models.CharField(max_length=50)
    books = models.ManyToManyField(Book)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Library"
        verbose_name_plural = "Libraries"

class Librarian(models.Model):
    name = models.CharField(max_length=50)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name} - {self.library.name}"
    
    class Meta:
        verbose_name = "Librarian"
        verbose_name_plural = "Librarians"


