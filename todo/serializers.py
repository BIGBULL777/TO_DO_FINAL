from django.db.models import fields
from rest_framework import serializers
from tasks.models import *

class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = '__all__'

class Time_createdSerializers(serializers.ModelSerializer):
    class Meta:
        model = time
        fields = '__all__'
    