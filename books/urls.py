from django.urls import path
from .views import BookListCreateView, RankedBooksView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list'),
    path('rankedBooks/', RankedBooksView.as_view(), name='ranked-book-list'),
]