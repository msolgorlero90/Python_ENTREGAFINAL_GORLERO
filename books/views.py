from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Book

# --- Lista de libros ---
def book_list(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'books/book_list.html', {'books': books})

# --- Detalle de libro ---
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})

# --- Crear libro ---
@method_decorator(login_required, name='dispatch')
class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'genre', 'available']
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('book_list')

# --- Editar libro ---
@method_decorator(login_required, name='dispatch')
class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author', 'genre', 'available']
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('book_list')

# --- Borrar libro ---
@method_decorator(login_required, name='dispatch')
class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = reverse_lazy('book_list')