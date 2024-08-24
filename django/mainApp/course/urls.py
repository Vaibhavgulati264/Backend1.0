from django.urls import path
from . views import CourseViewset

urlpatterns = [
    path('course/', CourseViewset.as_view()),
    path('course/<int:id>', CourseViewset.as_view())
]