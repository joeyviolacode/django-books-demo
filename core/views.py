from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm

# book_list = [
#     {"author": "The Author1", "title": "This is the Title1", "description": "Description1", "year": 1990, "id": 0},
#     {"author": "The Author2", "title": "This is the Title2", "description": "Description2", "year": 2020, "id": 1},
# ]

# Create your views here.
def homepage(request):
    book_list = Book.objects.all()
    return render(request, "books/homepage.html", {"book_list_from_view": book_list})

def show_book(request, pk):
    book_from_db = get_object_or_404(Book, pk=pk)
    return render(request, "books/book_detail.html", {"book": book_from_db})

def add_book(request):
    if request.method == "GET":
        book_add_form = BookForm()
        return render(request, "books/add_book.html", {"form": book_add_form})
    else:
        book_add_form = BookForm(data=request.POST)
        if book_add_form.is_valid():
            book_add_form.save()
            return redirect(to="homepage")

def search(request):
    search_term = request.POST.get("term", [""])
    books = Book.objects.filter(author=search_term)
    return render(
        request,
        "books/search_results.html",
        {"books": books, "author_name": search_term}
    )
