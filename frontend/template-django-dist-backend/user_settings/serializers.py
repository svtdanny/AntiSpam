from rest_framework import serializers
from rest_meets_djongo import serializers as djongo_serializers
from .models import LearningSettings, ClassSettings, MailLists
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer): 
    LearnSets = serializers.PrimaryKeyRelatedField(many=True, queryset=LearningSettings.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'learn')

class LearningSettingsSerializer(serializers.ModelSerializer): 
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = LearningSettings
        fields = ('VolumeInbox', 'VolumeSpam', 'UsePredefinedModel', 'creator')

class ClassSettingsSerializer(serializers.ModelSerializer):  
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = ClassSettings
        fields = ('ClassSetsRadio', 'ClassSets', 'creator')

class MailListsSerializer(djongo_serializers.DjongoModelSerializer):  
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = MailLists
        fields = ('whiteList', 'blackList', 'creator')
   