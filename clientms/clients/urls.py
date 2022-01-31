from django.urls import path
from . import views
from .views import (
    ClientUpdateView,
    ClientDetailView,
    ClientDeleteView,
    ClientCreateView,
    CommentCreateView,
    VehicleCreateView,
    VehicleDetailView,
    VehicleUpdateView,
    VehicleDeleteView,

)

urlpatterns = [
    path('<int:pk>/edit/',
         ClientUpdateView.as_view(), name='client_edit'),
    path('<int:pk>/',
         ClientDetailView.as_view(), name='client_detail'),
    path('<int:pk>/delete/',
         ClientDeleteView.as_view(), name='client_delete'),
    path('new/', ClientCreateView.as_view(), name='client_new'),
    #    path('', ClientListView.as_view(), name='client_list'),
    path('', views.ClientListView.as_view(), name='client_list'),
    path('<int:pk>/add_comment/',
         CommentCreateView.as_view(), name='client_addcomment'),
    path('vehicle_list/', views.VehicleListView.as_view(), name='vehicle_list'),
    path('<int:pk>/vehicle/', VehicleDetailView.as_view(), name='vehicle_detail'),
    path('newvehicle/', VehicleCreateView.as_view(), name='vehicle_new'),
    path('<int:pk>/vehicle_edit/',
         VehicleUpdateView.as_view(), name='vehicle_edit'),
    path('<int:pk>/vehicle_delete/',
         VehicleDeleteView.as_view(), name='vehicle_delete'),

]
