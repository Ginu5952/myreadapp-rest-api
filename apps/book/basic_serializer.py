from rest_framework import serializers
from apps.book.models.author import Author
from apps.book.models.tag import Tag

#- **Client**: makes a request with `JSON` data
#- **JSONParser**: transforms the JSON into Python native data types: `null` -> `None`
#- **Serializer**: Performs what we call serialization to tranform the Python native data type to complex data types like `QuerySets` and `model objects`.
#- **Django ORM**: assist in saving in database


### Deserialization Process -> Response
#- **Serializer**: Takes in data from the django ORM in the form of complex data type and tranform them to native Python data types
#- **JSONRenderer**: Tranforms the native Python data type to JSON
#- **Client**: Receives the JSON data in the response body


class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    def create(self, validated_data):
        return Author.objects.get_or_create(**validated_data)
    

class TagSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)   
    name = serializers.CharField() 

    def create(self, validated_data):
        return Tag.objects.get_or_create(**validated_data)
    

