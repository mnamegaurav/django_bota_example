from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.ChatterBotAppView.as_view(), name='home'),
    path('api/chatterbot/get_reply/',views.ChatterBotApiView.as_view(), name='chatterbot_api'),
]