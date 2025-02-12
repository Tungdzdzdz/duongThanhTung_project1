# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book/book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, id=pk)
    return render(request, 'book/book_detail.html', {'book': book})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'book/add_book.html', {'form': form})