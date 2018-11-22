from django.contrib import admin

# Register your models here.

from .models import Subject
from .models import Stream

from .models import Topic
from .models import Assignment
from .models import AssignmentTopic
from .models import AssignmentDone
# Register your models here.

admin.site.register(Subject)
admin.site.register(Stream)

admin.site.register(Topic)
admin.site.register(Assignment)
admin.site.register(AssignmentTopic)
admin.site.register(AssignmentDone)
