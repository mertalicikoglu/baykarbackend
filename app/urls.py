# baykarbackend/app/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import TeamViewSet, PersonnelViewSet, PartViewSet, AircraftViewSet, register_user

# Router tanımlaması
router = DefaultRouter()
router.register(r'teams', TeamViewSet)
router.register(r'personnel', PersonnelViewSet)
router.register(r'parts', PartViewSet)
router.register(r'aircraft', AircraftViewSet)

# URL Yönlendirmeleri
urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('register/', register_user, name='register_user'),  # Yeni kullanıcı kayıt endpointi
]

