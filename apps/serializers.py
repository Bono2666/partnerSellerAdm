from .models import *
from rest_framework import serializers


class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = '__all__'


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = '__all__'
