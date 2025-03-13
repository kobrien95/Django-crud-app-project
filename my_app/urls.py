from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='name'),
    path('about/',views.about, name='about'),
    path('trucks/', views.truck_index, name='truck-index'),
]