from rest_framework import serializers
from .models import Course

class CourseSerialize(serializers.ModelSerializer):
    class Meta: 
        app_label = 'courseSerializes'
        model = Course
        fields = ('id','name','description','code')