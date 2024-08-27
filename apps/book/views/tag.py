from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.response import Response
from rest_framework import status
from apps.book.models import Tag
from apps.book.serializer import TagSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

"""
curl http://127.0.0.1.8000/api/v1/book/tag/
token_header = 'Authentication: Token 8c77ffe9946181bc30c823b3b4e2fed4b20beae0'

curl -H 'Authorization: Token 8c77ffe9946181bc30c823b3b4e2fed4b20beae0' http://127.0.0.1:8000/api/v1/book/tag/


"""


@api_view() # Define our http methods
#@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def list_tags(request):
    # ORM
    tags = Tag.objects.all() # Complex Data type

    # DeSerialization
    data = TagSerializer(tags, many=True) # Convert complex data type to primitive Python types

    # Return JSOn
    return Response(data.data, status=status.HTTP_200_OK)