from django.forms import Textarea
from django.contrib import admin
from .models import Entry

# Register your models here.
admin.site.register(Entry)

class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    #working on admin customization