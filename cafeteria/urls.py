"""cafeteria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from api.urls import urlpatterns

schema_url_patterns = [
    path('', include(urlpatterns)),
]

schema_view_v1 = get_schema_view(
    openapi.Info(
        title='Cafeteria Menu API',
        default_version='v1',
        description='국제기능올림픽대회 훈련센터 통합 식단 API'
    ),
    public=True,
    permission_classes=[AllowAny],
    patterns=schema_url_patterns
)

urlpatterns = [
    path('api/v1/', include(urlpatterns)),
    path('swagger<str:format>', schema_view_v1.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view_v1.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view_v1.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
]
