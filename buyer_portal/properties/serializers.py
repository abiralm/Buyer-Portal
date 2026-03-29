from rest_framework import serializers
from .models import Property,Favourite

class PropertySerilizer (serializers.ModelSerializer):
    
    class Meta:
        model = Property
        fields = '__all__'

class FavouritesSerializer(serializers.ModelSerializer):

    property = PropertySerilizer(read_only=True)
    property_id = serializers.PrimaryKeyRelatedField(queryset=Property.objects.all(),write_only=True, source='property')

    class Meta:
        model = Favourite
        fields = ['id', 'property', 'property_id', 'created_at']

