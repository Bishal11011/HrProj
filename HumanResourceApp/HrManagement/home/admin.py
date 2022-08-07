from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Provinces)
admin.site.register(Specialization)



from django.contrib import admin

from .models import *
# Register your models here.


@admin.register(CustomUser)
class CustomUserrAdmin(admin.ModelAdmin):
    list_filter = ('provinces', 'specialization')
    list_display = ['id', 'first_name', 'last_name', 'provinces', 'specialization','address','updated','email']

