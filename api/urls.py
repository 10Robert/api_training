from django.urls import path, include
from api import view_api
from .views import index
from django.contrib import admin
from rest_framework.routers import SimpleRouter


user_api_router = SimpleRouter()
user_api_router.register(
    'api',
    view_api.UserListViewSet,)

urlpatterns = [
        path('home_api', index, name='index'),
        path(
        'api/conta/<int:pk>/',
        view_api.conta_api_detail,
        name='conta_api_detail',
         ),
        
        path(
        'api/conta',
        view_api.conta_api,
        name='api_conta'
             ),
        
         path('', include(user_api_router.urls))
]
