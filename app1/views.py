from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView,ListView,CreateView,DeleteView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from .forms import BookForm
from .models import Book

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'

## function based views

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name= fs.save(uploaded_file.name,uploaded_file)
        # url = fs.url(name)      #/media/emp_info_csv_Er3cdzR
        context['url'] = fs.url(name)
        # print(url)
        print(uploaded_file.name)
        print(uploaded_file.size)
    return render(request,'upload.html',context)

def book_list(request):
    books = Book.objects.all()
    return render(request,'book_list.html',{'books':books})

def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = BookForm()
    return render(request,'upload_book.html',{'form': form})

class BookListView(ListView):
    model = Book
    template_name = 'class_books_list.html'
    context_object_name = 'books'

class UploadBookView(CreateView):
    model = Book
    fields = ('title','author','pdf','cover')
    success_url = reverse_lazy('class_book_view')
    template_name = 'upload_book.html'

def delete_book(request,pk):
    if request.method == 'POST':
        book = Book.objects.get(pk=pk)
        book.delete()
    return redirect('books')

def delete_all_book(request):
    if request.method == 'POST':
        books = Book.objects.all()
        for book in books:
            # print(book)
            book.delete()
    return HttpResponse("successfully deleted the data")

# class DeleteAllBook(DeleteView):
#     model = Book
    
#     def post(self, request):
#         books = Book.objects.all()
#         for book in books:
#             book.delete()
#         return redirect("book_list")
