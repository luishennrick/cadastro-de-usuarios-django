from appcaduser import views

from django.contrib import admin

from django.urls import path, include

from rest_framework.routers import SimpleRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

user_api_router = SimpleRouter()
user_api_router.register(
    'api/list/usuario',
    views.UserApiListViewSet,
    basename='user-api'
)

urlpatterns = [
   
    path('admin/', admin.site.urls),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('', include(user_api_router.urls)),
] 