from django.contrib import admin

# Register your models here.

from .models import Individuals, Specimens, Checkout
admin.site.register(Specimens),
admin.site.register(Check),
admin.site.register(Individuals),