
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.http import JsonResponse
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


from django.conf.urls.static import static

def api_root(request):
    return JsonResponse({
        "message": "API root",
        "endpoints": {
            "auth_token": "/api/auth/token/",
            "auth_refresh": "/api/auth/token/refresh/",
            "accounts": "/api/accounts/",
            "profiles": "/api/profiles/",
            "interactions": "/api/interactions/",
            "invites": "/api/invites/"
        }
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_root, name='api-root'),
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/accounts/', include('accounts.urls')),
    path('api/profiles/', include('profiles.urls')),
    path('api/interactions/', include('interactions.urls')),
    path('api/invites/', include('invites.urls')),
  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

