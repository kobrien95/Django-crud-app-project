from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/',views.about, name='about'),
    path('trucks/', views.truck_index, name='truck-index'),
    path('trucks/<int:truck_id>/', views.truck_detail, name='truck-detail'),
    path('trucks/create/', views.TruckCreate.as_view(), name='truck-create'),
    path('trucks/<int:pk>/update/', views.TruckUpdate.as_view(), name ='truck-update'),
    path('trucks/<int:pk>/delete/', views.TruckDelete.as_view(), name ='truck-delete'),
    path('accounts/signup/', views.signup, name='signup'),

]