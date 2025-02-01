from rest_framework import serializers
from .models import Course, Progress

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class ProgressSerializer(serializers.ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = Progress
        fields = '__all__'
