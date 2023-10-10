from appcaduser import views

from django.urls import path

urlpatterns = [

    path('', views.site.home, name='home'),

    path('usuarios/', views.site.usuarios, name='lista'),

    path(
        'user/api/v1',
        views.user_api_list,
        name='user/api/v1'
    )
  
]
