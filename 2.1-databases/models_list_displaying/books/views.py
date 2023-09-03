from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from books.models import Book


def index(request):
    return redirect('books')


def books_view(request):
    template = 'books/books_list.html'
    context = {'books': Book.objects.all()}
    return render(request, template, context)


def show_books_by_pub_date(request, pub_date):
    template = 'books/books_list.html'
    books = Book.objects.all()
    paginator = Paginator(books, 10)
    page_date = request.GET.get('pub_date')
    page = paginator.get_page(page_date)
    prev = Book.objects.filter(pub_date__lt=pub_date).values('pub_date').first()
    if prev is not None:
        prev = prev['pub_date'].strftime('%Y-%m-%d')
    next = Book.objects.filter(pub_date__gt=pub_date).values('pub_date').first()
    if next is not None:
        next = next['pub_date'].strftime('%Y-%m-%d')
    context = {
        'page': page,
        'pub_date': pub_date,
        'books': Book.objects.filter(pub_date=pub_date),
        'prev': prev,
        'next': next,
    }
    return render(request, template, context)
