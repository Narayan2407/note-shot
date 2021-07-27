from django.contrib import admin
from .models import sem, course, course_pdf

admin.site.register(sem)
admin.site.register(course)
admin.site.register(course_pdf)