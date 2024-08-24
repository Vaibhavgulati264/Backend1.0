from django.urls import path
from . views import CourseViewset

urlpatterns = [
    path('instance/', CourseViewset.as_view()),
    path('instance/<int:id>', CourseViewset.as_view())
]