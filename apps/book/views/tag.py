from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from apps.book.models import Tag
from apps.book.serializer import TagSerializer

#Function-base view
@api_view() # by default , it uses a 'GET' method
def list_tags(request):
    # Get all authors using ORM
    tags = Tag.objects.all()

    # Deserialize using the AuthorSerializer
    data = TagSerializer(tags, many=True)

    return Response(data.data, status=status.HTTP_200_OK)