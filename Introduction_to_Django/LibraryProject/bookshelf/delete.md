Book.objects.get(id = 1).delete()
<!-- (1, {'bookshelf.Book': 1}) -->

Book.objects.all()
<!-- <QuerySet []> -->