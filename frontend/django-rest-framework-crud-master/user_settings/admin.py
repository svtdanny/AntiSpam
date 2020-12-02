from django.contrib import admin
from . models import  LearningSettings, ClassSettings, MailLists
# Register your models here.

admin.site.register(LearningSettings)
admin.site.register(ClassSettings)
admin.site.register(MailLists)