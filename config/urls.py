from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Company and Movie API",
      default_version='v1',
      description="DRF Basic token / Token bilan himoyalangan API",
      contact=openapi.Contact(email="akramjonakbaraliev2010l@gmail.com"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/movies/', include('movie.urls')),
    path('api/company/', include('company.urls')),
    path('api/token/', views.obtain_auth_token),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
