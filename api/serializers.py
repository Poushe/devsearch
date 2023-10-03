from rest_framework import serializers
from projects.models import Project
from users.models import profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=profile
        fields= '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    owner=ProfileSerializer(many=False)
    class Meta:
        model=Project
        fields= '__all__'