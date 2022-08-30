from django.contrib import admin

# Register your models here.
from app15.models import Studreg
from app15.models import Empreg,User


admin.site.register(Studreg)
admin.site.register(Empreg)
admin.site.register(User)
