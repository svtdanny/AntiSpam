from django.contrib import admin
from . models import  LearningSettings, ClassSettings
# Register your models here.

admin.site.register(LearningSettings)
admin.site.register(ClassSettings)