from django.db.models import Window, F
from django.db.models.functions import RowNumber
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

class BookListCreateView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class RankedBooksView(APIView):
    def get(self, request):
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        if not start_date or not end_date:
            return Response({"error": "Both start_date and end_date are required."}, status=400)

        books = Book.objects.filter(
            publication_date__range=[start_date, end_date]
        ).annotate(
            rank=Window(
                expression=RowNumber(),
                order_by=F('page_count').desc()
            )
        ).values('id', 'title', 'page_count', 'rank')

        return Response(books)