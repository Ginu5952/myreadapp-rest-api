from rest_framework import serializers
from apps.book.models import Author

class AuthorSerializer(serializers.ModelSerializer):
    #TODO: Specify the model that this serializer will link to
    # TODO: Specify which fields should be considered in the model

    # Force django REST to recognize the model's method
    name = serializers.CharField() # read-only
    # Create a serialized method
    username = serializers.SerializerMethodField()

    # Serialzied method's implementation
    def get_username(self, obj): # get_<serializeer_method_field>
        # obj is the model's object
        return '_'.join([obj.first_name, obj.last_name])


    def validate_first_name(self, value): # validate_<field-name>
        """Field-Level Validation"""

        if '-' in value:
            # TODO: Always raise a validation exception when condition fails
            raise serializers.ValidationError('first name should not contain hyphen (-)')
        
        # TODO: If condition is true, then return the value
        return value
    
    def validate(self, attrs): # valide
        """Object-Level Validation"""
        
        if attrs.get('first_name') == attrs.get('last_name'):
            raise serializers.ValidationError('first name and last name should not be the same')
        
        return attrs

    class Meta:
        model = Author
        fields = "__all__" #  ('id', 'first_name', 'first_name', 'name', 'username')
        read_only_fields = ('id', )