from django.contrib import admin

from .models import Team, Game

class TeamAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'last_modified')

class GameAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'last_modified') 

# Register your models here.
admin.site.register(Team, TeamAdmin)
admin.site.register(Game, GameAdmin)
