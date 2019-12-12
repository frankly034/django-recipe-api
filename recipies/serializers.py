from rest_framework import serializers
from recipies.models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Recipe
    fields = '__all__'