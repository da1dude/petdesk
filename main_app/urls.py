from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pets/', views.pets_index, name='index'),
    path('pets/<int:pet_id>/', views.pets_detail, name='detail'),
    path('pets/create/', views.PetCreate.as_view(), name='pets_create'),
<<<<<<< HEAD
    path('pets/<int:pk>/update/', views.PetUpdate.as_view(), name='pets_update'),
=======
    path('pets/<int:pk>/delete', views.PetDelete.as_view(), name='pets_delete'),
>>>>>>> e7253d098797c889e5df748fc27496e250869b4b


    #Auth URLs
    path('accounts/signup/', views.signup, name='signup'),
]