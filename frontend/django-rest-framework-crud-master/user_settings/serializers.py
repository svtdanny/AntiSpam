from rest_framework import serializers
from .models import LearningSettings, ClassSettings
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):  # create class to serializer usermodel
    LearnSets = serializers.PrimaryKeyRelatedField(many=True, queryset=LearningSettings.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'learn')

class LearningSettingsSerializer(serializers.ModelSerializer):  # create class to serializer model
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = LearningSettings
        fields = ('VolumeInbox', 'VolumeSpam', 'UsePredefinedModel', 'creator')

class ClassSettingsSerializer(serializers.ModelSerializer):  # create class to serializer model
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = ClassSettings
        fields = ('ClassSetsRadio', 'ClassSets', 'creator')
   