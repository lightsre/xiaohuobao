from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('webinfo/', views.web_info, name='web_info'),
    path('login/', views.login_view, name='login_view'),
    path('namesee/', views.web_name_see, name='name_see'),
    path('insee/', views.web_trade_see, name='in_see'),
    path('outsee/', views.web_trade_see, name='out_see'),
    path('profitsee/', views.web_profit_see, name='profit_see'),
]
