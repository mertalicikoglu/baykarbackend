# baykarbackend/baykarbackend/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger API Dokümantasyonu için yapılandırma
schema_view = get_schema_view(
   openapi.Info(
      title="Hava Aracı Üretim API",
      default_version='v1',
      description="Hava aracı üretim uygulaması için API dokümantasyonu",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Django yönetim paneli için URL
    path('admin/', admin.site.urls),

    # Ana uygulama API'sine yönlendirme
    path('', include('app.urls')),  # 'app' ismini, kendi uygulamanızın adıyla değiştirin

    # Swagger Dokümantasyonu için URL
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
