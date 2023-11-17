from appcaduser import views

from django.urls import path

urlpatterns = [

    path('', views.site.home, name='home'),

    path('usuarios/', views.site.usuarios, name='lista'),

    path(
        'user/api/v1',
        views.UserApiListViewSet.as_view({
            'get': 'list',
            'post': 'create'
        }),
        name='user_api_v1'
    ),

    path(
        'user/api/v1/<int:pk>/',
        views.UserApiListViewSet.as_view({
            'get': 'retrieve',
            'patch': 'partial_update',
            'delete': 'destroy'
        }),
        name='user_api_v1_detail'
    ),
  
]
