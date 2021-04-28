from djongo import models
from rest_framework import serializers 

# Create your models here.
class LearningSettings(models.Model):
    VolumeInbox = models.IntegerField()
    VolumeSpam = models.IntegerField()
    UsePredefinedModel = models.BooleanField()

    creator = models.ForeignKey('auth.User', related_name='user_settings', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.creator) + '_learn_sets'

class ClassSettings(models.Model):
    ClassSetsRadio = models.CharField(max_length=15)
    ClassSets = models.FloatField()

    creator = models.ForeignKey('auth.User', related_name='user_class_settings', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.creator) + '_class_sets'

class MailLists(models.Model):
    _id = models.ObjectIdField()
    
    whiteList = models.TextField(null=True, blank=True)
    blackList = models.TextField(null=True, blank=True)

    creator = models.ForeignKey('auth.User', related_name='user_mail_lists', on_delete=models.CASCADE)

    objects = models.DjongoManager()

    def __str__(self):
        return str(self.creator) + '_mail_lists'
    """
    def insert_mailist(self, index, value):
        self.mylist.insert(index, value)
        #self.save()
    def remove_from_mylist(self, value):
        self.mylist.remove(value)
        #self.save()
    """

class LastLearn(models.Model):
    lastLearn = models.CharField(max_length=30)
    totalTime = models.CharField(max_length=30)

    VolumeInbox = models.IntegerField()
    VolumeSpam = models.IntegerField()


    creator = models.ForeignKey('auth.User', related_name='user_lastlearn', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.creator) + '_lastlearn'
    