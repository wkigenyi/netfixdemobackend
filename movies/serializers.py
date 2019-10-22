from rest_framework import serializers
from .models import Director,Actor,Movie

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'
    
class MovieSerializer(serializers.ModelSerializer):
    director = serializers.StringRelatedField()
    writer = serializers.StringRelatedField()
    rated = serializers.StringRelatedField()
    country = serializers.StringRelatedField()
    language = serializers.StringRelatedField()
    actors = serializers.StringRelatedField(many=True)
    awards = serializers.StringRelatedField(many=True)  
    genres = serializers.StringRelatedField(many=True) 
      
    class Meta:
        model = Movie
        fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'
