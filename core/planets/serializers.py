#Serializer implementation for actions into the database
from rest_framework import serializers
from .models import Planet

class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = ['name', 'population', 'terrains', 'climates']

    def create(self, validated_data):
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.population = validated_data.get('population', instance.population)
        instance.terrains = validated_data.get('terrains', instance.terrains)
        instance.climates = validated_data.get('climates', instance.climates)
        instance.save()
        return instance
