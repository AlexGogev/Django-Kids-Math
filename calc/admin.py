from django.contrib import admin
from .models import Adding, Star
# Register your models here.


class PersonAdmin(admin.ModelAdmin):
    list_display = ['id',"correct","wrong","data","time","user"]
admin.site.register(Adding, PersonAdmin)

admin.site.register(Star)