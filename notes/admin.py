from django.contrib import admin

# Register your models here.
from .models import Notes

class NoteAdmin(admin.ModelAdmin):
	readonly_fields=('created_at', 'last_modified')

admin.site.register(Notes, NoteAdmin)