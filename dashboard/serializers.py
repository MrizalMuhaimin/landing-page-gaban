from rest_framework import serializers
from .models import InfoUser, Jurusan, Kampus

class InfoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model= InfoUser
        fields = '__all__'


class InfoJurusanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jurusan
        fields = '__all__'
    
class InfoKampusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kampus
        fields = '__all__'