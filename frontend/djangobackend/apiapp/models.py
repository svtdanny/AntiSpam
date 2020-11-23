from django.db import models

from  django.core.validators import MinValueValidator, MaxValueValidator

class Posts (models.Model):

    title = models.CharField(max_length=250)
    content = models.TextField()

    def __str__(self):
        return self.title

class LearnSets (models.Model):

    max_vol_train = models.IntegerField(default=250, validators=[MinValueValidator(1), MaxValueValidator(2000)])
    max_vol_spam = models.IntegerField(default=250, validators=[MinValueValidator(1), MaxValueValidator(2000)])