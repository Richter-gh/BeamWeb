from django.contrib import admin

# Register your models here.
from sopromat_beam.models import beam_tasks, beam_attempts

admin.site.register(beam_tasks)
admin.site.register(beam_attempts)