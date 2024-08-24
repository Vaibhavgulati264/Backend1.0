from rest_framework import serializers
from .models import Instance

class InstanceSerialize(serializers.ModelSerializer):
    class Meta: 
        app_label = 'instanceSerializes'
        model = Instance
        fields = ('id','name','year','semester','code')