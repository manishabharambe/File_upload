from app1.models import Book

ans1 = Book.objects.values_list('title',flat=True) ## will print single value..default
ans2 = Book.objects.values_list('title',flat=False) ## will give list of tuple of single value..if passed multiple value it raise error
print(ans1)
print(ans2)