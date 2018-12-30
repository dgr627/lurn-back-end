from rest_framework.serializers import ModelSerializer

from .models import *

class LessonSerializer(ModelSerializer):
	class Meta:
		model = Lesson
		fields = '__all__'