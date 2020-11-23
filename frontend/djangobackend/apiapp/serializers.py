from rest_framework import serializers
from .models import Posts, LearnSets


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'

class LearnSetsSerializer(serializers.ModelSerializer):

    class Meta:
        model = LearnSets

    def save(self):
        user = self.context['request'].user
        title = self.validated_data['title']
        article = self.validated_data['article']