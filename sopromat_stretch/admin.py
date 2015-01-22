from django.contrib import admin

# Register your models here.
from sopromat_stretch.models import stretch_tasks, stretch_attempts

admin.site.register(stretch_tasks)
admin.site.register(stretch_attempts)