from django.contrib import admin

# Register your models here.

from .models import Subject
from .models import Stream

admin.site.register(Subject)
admin.site.register(Stream)
