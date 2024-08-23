
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from apps.book.models import Author
from apps.book.serializer import AuthorSerializer

#Function-base view
@api_view(['GET']) # by default , it uses a 'GET' method
def list_authors(request):
    # Get all authors using ORM
    authors = Author.objects.all()

    # Deserialize using the AuthorSerializer
    data = AuthorSerializer(authors, many=True)

    return Response(data.data, status=status.HTTP_200_OK)