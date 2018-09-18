from django.contrib import admin
from .models import Note

class NoteAdmin(admin.ModelAdmin):       #This class allows us to see the readonly fields we created in out Notes model
    readonly_fields=('created_at', 'last_modified')

# Register your models here.

admin.site.register(Note, NoteAdmin)

