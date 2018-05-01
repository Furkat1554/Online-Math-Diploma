# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Topic
from .models import Assignment
from .models import AssignmentTopic
# Register your models here.

admin.site.register(Topic)
admin.site.register(Assignment)
admin.site.register(AssignmentTopic)
