from django.contrib import admin

from .models import Smurf

class SmurfAdmin(admin.ModelAdmin): # To get the read-only fields to show up in the interface
	readonly_fields=('created_at', 'last_modified')

# Register your models here.
admin.site.register(Smurf, SmurfAdmin) # register the Smurf model with the admin site 
