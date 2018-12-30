from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Lesson)
admin.site.register(UserCard)
admin.site.register(Question)
admin.site.register(Choice)
