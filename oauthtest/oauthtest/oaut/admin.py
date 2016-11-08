from django.contrib import admin

from oauthtest.oaut.models import Envelope
# Register your models here.

class ClassAdmin(admin.ModelAdmin):
    list_display = ['id','date_due','exam_start','exam_duration']

admin.site.register(Envelope,ClassAdmin);