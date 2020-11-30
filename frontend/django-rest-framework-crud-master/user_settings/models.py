from django.db import models

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