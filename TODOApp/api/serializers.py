from dataclasses import fields
from rest_framework import serializers
from TODOApp.models import TODO

class TODOSerializer(serializers.ModelSerializer):
    class Meta:
        model = TODO
        fields = '__all__'