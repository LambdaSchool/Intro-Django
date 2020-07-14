from django.contrib import admin

from .models import Card

class CardAdmin(admin.ModelAdmin):
    readonly_fields=('created_at', 'last_modified')

# Register your models here.
admin.site.register(Card, CardAdmin)