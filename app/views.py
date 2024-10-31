# baykarbackend/app/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, permission_classes
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from .models import Team, Personnel, Part, Aircraft
from .serializers import TeamSerializer, PersonnelSerializer, PartSerializer, AircraftSerializer, UserSerializer
from rest_framework import serializers

# Takım ViewSet (TeamViewSet)
class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated]

# Personel ViewSet (PersonnelViewSet)
class PersonnelViewSet(viewsets.ModelViewSet):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer
    permission_classes = [IsAuthenticated]

# Parça ViewSet (PartViewSet)
class PartViewSet(viewsets.ModelViewSet):
    queryset = Part.objects.all()
    serializer_class = PartSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Her takım sadece kendi parça türünü üretebilir
        team = serializer.validated_data['team']
        part_type = serializer.validated_data['type']
        if not self.validate_team_part(team, part_type):
            raise serializers.ValidationError(f"{team.name} bu tip parçayı üretemez.")
        serializer.save()

    def validate_team_part(self, team, part_type):
        # Örnek kontrol: Her takım yalnızca kendi türünde parça üretebilir
        team_part_mapping = {
            'Kanat Takımı': 'wing',
            'Gövde Takımı': 'body',
            'Kuyruk Takımı': 'tail',
            'Aviyonik Takımı': 'avionics'
        }
        return team_part_mapping.get(team.name) == part_type

# Uçak ViewSet (AircraftViewSet)
class AircraftViewSet(viewsets.ModelViewSet):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def assemble(self, request, pk=None):
        aircraft = self.get_object()
        required_parts = ['wing', 'body', 'tail', 'avionics']
        missing_parts = [
            part for part in required_parts 
            if not aircraft.parts.filter(type=part).exists()
        ]

        if missing_parts:
            return Response(
                {"message": f"Eksik parçalar: {', '.join(missing_parts)}"}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        aircraft.assembled = True
        aircraft.save()
        return Response({"message": "Uçak başarıyla monte edildi."})

# Kullanıcı kayıt işlemi için view
@api_view(['POST'])
@permission_classes([AllowAny])  # Herkesin bu API'yi çağırabilmesi için
def register_user(request):
    """Yeni bir kullanıcıyı sisteme kaydetmek için API"""
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Kullanıcı için token oluştur
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
