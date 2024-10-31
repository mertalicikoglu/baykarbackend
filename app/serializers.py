# baykarbackend/app/serializers.py

from rest_framework import serializers
from .models import Team, Personnel, Part, Aircraft
from django.contrib.auth.models import User
from rest_framework import serializers

# Takım Serileştiricisi (Team Serializer)
class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name']

# Personel Serileştiricisi (Personnel Serializer)
class PersonnelSerializer(serializers.ModelSerializer):
    team_name = serializers.CharField(source='team.name', read_only=True)

    class Meta:
        model = Personnel
        fields = ['id', 'name', 'team', 'team_name']

# Parça Serileştiricisi (Part Serializer)
class PartSerializer(serializers.ModelSerializer):
    team_name = serializers.CharField(source='team.name', read_only=True)
    aircraft_name = serializers.CharField(source='get_aircraft_type_display', read_only=True)

    class Meta:
        model = Part
        fields = ['id', 'type', 'aircraft_type', 'team', 'team_name', 'status', 'aircraft_name']

# Uçak Serileştiricisi (Aircraft Serializer)
class AircraftSerializer(serializers.ModelSerializer):
    parts = PartSerializer(many=True, read_only=True)

    class Meta:
        model = Aircraft
        fields = ['id', 'type', 'parts', 'assembled']


# Kullanıcı Serileştiricisi
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Şifreyi hashleyerek kullanıcı oluşturur
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user