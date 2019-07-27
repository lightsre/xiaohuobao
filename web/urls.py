from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('webinfo/', views.web_info, name='web_info'),
    path('login/', views.login_view, name='login_view'),
    path('nameinput/', views.web_name_input, name='name_input'),
    path('namesee/', views.web_name_see, name='name_see'),
    path('ininput/', views.web_in_input, name='in_input'),
    path('insee/', views.web_in_see, name='in_see'),
    path('outinput/', views.web_out_input, name='out_input'),
    path('outsee/', views.web_out_see, name='out_see'),
    path('profitsee/', views.web_profit_see, name='profit_see'),
]
