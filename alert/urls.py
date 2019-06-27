
from django.urls import path
from alert import views

app_name = 'alert'

urlpatterns = [
    path('', views.alert),
    path('alert/', views.AlertView.as_view(), name='alert-sound')
]
