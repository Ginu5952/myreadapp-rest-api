from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveAPIView, DestroyAPIView, RetrieveDestroyAPIView
from apps.book.models import Author 
from apps.book.serializer import AuthorSerializer

"""
curl http://127.0.0.1:8000/api/v1/book/author/

curl -u admin:admin http://127.0.0.1:8000/api/v1/book/author/

"""
# Function-base view
@api_view(['GET'])  # By default, it uses a 'GET' method
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def list_authors(request):
    # Get all authors using ORM
    authors = Author.objects.all()

    # Deserialize using the AuthorSerializer
    data = AuthorSerializer(authors, many=True)

    # Return data
    return Response(data.data, status=status.HTTP_200_OK)


"""
curl http://127.0.0.1:8000/api/v1/book/author/1

curl -u admin:admin http://127.0.0.1:8000/api/v1/book/author/1

"""
class DetailAuthor(RetrieveDestroyAPIView):
    # How do we handle generic views
    # ORM
    queryset = Author.objects.all()
    # Serializer
    serializer_class = AuthorSerializer

    # Authentication: Delcare an authentication scheme to be used
    authentication_classes = (BasicAuthentication, )

    # Permissions: IsAuthenticated triggers the authentiation proces to take place
    permission_classes = (IsAuthenticated, )


class DeleteAuthor(DestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer