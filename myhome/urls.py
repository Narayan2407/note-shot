from django.urls import path
from django.conf.urls import url
from .views import index,courses, notes

urlpatterns = [
path("", index, name="Index"),
path("courses/", courses, name="Courses"),
path("notes/", notes, name="notes")
]