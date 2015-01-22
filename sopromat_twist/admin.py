from django.contrib import admin

# Register your models here.
from sopromat_twist.models import twist_tasks, twist_attempts

admin.site.register(twist_tasks)
admin.site.register(twist_attempts)