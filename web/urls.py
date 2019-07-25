from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('web-info/', views.web_info, name='web_info'),
]
