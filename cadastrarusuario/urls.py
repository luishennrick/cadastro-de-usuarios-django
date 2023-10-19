from appcaduser import views

from django.urls import path

urlpatterns = [

    path('', views.site.home, name='home'),

    path('usuarios/', views.site.usuarios, name='lista'),

    path(
        'user/api/v1',
        views.UserApiList.as_view(),
        name='user_api_v1'
    ),

    path(
        'user/api/v1/<int:pk>/',
        views.UserApiListDetail.as_view(),
        name='user_api_v1_detail'
    ),
  
]
