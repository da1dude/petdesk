from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pets/', views.pets_index, name='index'),
    path('pets/<int:pet_id>/', views.pets_detail, name='detail'),
    path('pets/create/', views.PetCreate.as_view(), name='pets_create'),
    path('pets/<int:pk>/update/', views.PetUpdate.as_view(), name='pets_update'),
    path('pets/<int:pk>/delete', views.PetDelete.as_view(), name='pets_delete'),
    path('pets/<int:pet_id>/add_checkin/', views.add_checkin, name='add_checkin'),

    #Rx URLS
    path('rxs/', views.RxList.as_view(), name='rxs_index'),
    path('rxs/<int:pk>/delete', views.RxDelete.as_view(), name='rxs_delete'),
    path('rxs/<int:pk>/update/', views.RxUpdate.as_view(), name='rxs_update'),
    path('rxs/<int:pk>/', views.RxDetail.as_view(), name='rxs_detail'),

    #checkin URLS
    path('checkins/<int:pk>/', views.CheckinDetail.as_view(), name='checkin_detail'),

    #Auth URLs
    path('accounts/signup/', views.signup, name='signup'),
]