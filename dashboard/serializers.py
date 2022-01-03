from rest_framework import serializers
from .models import InfoUser

class InfoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model= InfoUser
        fields = '__all__'
