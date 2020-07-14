from django.contrib import admin

from .models import Meal, PersonalMeal

# Register your models here.


class MealAdmin(admin.ModelAdmin):
    readonly_fields = ['date']


admin.site.register((Meal, PersonalMeal), MealAdmin)