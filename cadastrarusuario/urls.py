from appcaduser import views

from django.urls import path

from rest_framework.routers import SimpleRouter

user_api_router = SimpleRouter()
user_api_router.register(
    'api/list/usuario',
    views.UserApiListViewSet
)

urlpatterns = user_api_router.urls