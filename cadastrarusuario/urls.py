from appcaduser import views

from django.urls import path

urlpatterns = [

    path('', views.site.home, name='home'),

    path('usuarios/', views.site.usuarios, name='lista'),

    path(
        'user/api/v1',
        views.user_api_list,
        name='user_api_v1'
    ),

    path(
        'user/api/v1/<int:pk>/',
        views.user_api_detail,
        name='user_api_v1_detail'
    ),
  
]
