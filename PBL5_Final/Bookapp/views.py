from django.shortcuts import render
from .models import Book, Category
from django.core.paginator import Paginator
from django.shortcuts import render,redirect,get_list_or_404,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import *
# Create your views here.
@login_required(login_url='jlpt:Login')
def home(request):
    recommended_books = Book.objects.filter(recommended_books=True)
    reading_book = Book.objects.filter(reading_books=True)
    grammar_books = Book.objects.filter(grammar_books=True)
    vocabulary_books = Book.objects.filter(vocabulary_books=True)
    listen_books = Book.objects.filter(listen_books=True)
    tips_books = Book.objects.filter(tips_books=True)
    return render(request, 'Book/home.html',{'recommended_books':recommended_books,'reading_book':reading_book,'grammar_books':grammar_books,
                                        'vocabulary_books':vocabulary_books,'listen_books':listen_books,'tips_books':tips_books})

@login_required(login_url='jlpt:Login')
def all_books(request):
    books = Book.objects.all()
    return render(request, 'Book/all_books.html', {'books':books})

@login_required(login_url='jlpt:Login')
def category_detail(request, slug):
    category = Category.objects.get(slug = slug)
    return render(request, 'Book/genre_detail.html',{'category':category})

@login_required(login_url='jlpt:Login')
def book_detail(request, slug):
    book = Book.objects.get(slug = slug)
    book_category = book.category.first()
    similar_books = Book.objects.filter(category__name__startswith = book_category)
    return render(request, 'Book/book_detail.html', {'book':book, 'similar_books': similar_books})

@login_required(login_url='jlpt:Login')
def search_book(request):
    search_books = Book.objects.filter(title__icontains = request.POST.get('name_of_book'))
    return render(request, 'Book/search_book.html',{'search_books':search_books})

@login_required(login_url='jlpt:Login')
def book_list(request,number):
    search = request.GET.get('search')
    if search == '' or search is None:
        search = ''
        book = Book.objects.all().filter(user=request.user)
    else:
        book = Book.objects.filter(name__icontains = search)
    paginator = Paginator(book,10)
    page_obj = paginator.page(number)
    context = {
        'page_obj' : page_obj,
        'search' :search,
        'number' : number
    }
    return render(request,'Book/books_list.html',context)

# def book_list(request,number):
#     search = request.GET.get('search')
#     if search == '' or search is None:
#         search = ''
#         book = Book.objects.all().filter(user=request.user)
#     else:
#         book = Book.objects.filter(name__icontains = search)
#     paginator = Paginator(book,10)
#     page_obj = paginator.page(number)
#     context = {
#         'page_obj' : page_obj,
#         'search' :search,
#         'number' : number
#     }
#     return render(request,'Document/document_list.html',context)
@login_required(login_url='jlpt:Login')
def edit_book(request,pk):
    book = get_object_or_404(Book,id = pk)
    if request.method == "POST":
        print("POST")
        form = AddBookForm(request.POST, request.FILES,instance = book)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('Teacher:DetailBook',pk=form.instance.id)
        else:
            print("Form is not valid")
            print(form.cleaned_data)
    form = AddBookForm(instance=book)
    return render(request,'Book/edit_book_form.html',{'form' : form})