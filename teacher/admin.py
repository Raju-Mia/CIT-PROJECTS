from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Teacher)
admin.site.register(SeniorTeacher)
admin.site.register(JuniorTeacher)

admin.site.register(Parent)
admin.site.register(Child)