from django.contrib import admin
from .models import Fire, Comment, UpdateTime


# Register your models here.
admin.site.register(Fire)
admin.site.register(Comment)
admin.site.register(UpdateTime)