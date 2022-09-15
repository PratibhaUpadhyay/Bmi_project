from django.contrib import admin
from .models import Bmi

# Register your models here.
class Admin(admin.ModelAdmin):
    list_display = ('weight','height','age','gender',' claculate bmi')
admin.site.register(Bmi, BmiAdmin)


