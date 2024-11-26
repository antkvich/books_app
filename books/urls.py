from django.urls import path
from .views import BookListCreateView, RankedBooksView, BookDetailView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list'),
    path('rankedBooks/', RankedBooksView.as_view(), name='ranked-book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail')
]