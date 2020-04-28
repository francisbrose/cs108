from django.contrib import admin

# Register your models here.

from .models import Specimen, Individual, Check
admin.site.register(Specimen)
admin.site.register(Individual)
admin.site.register(Check)