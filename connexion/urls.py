from django.urls import path

from .views import connexion,register,deconnexion,profil,profil_management,delete_account

urlpatterns = [
    path('login/',connexion,name="login"),
    path('register/',register,name="register"),
    path('profil/',profil,name="profil"), 
    path('profil-management/',profil_management,name="profil-management"),
    path('delete-account/',delete_account,name="delete-account"),          
    path('deconnexion/',deconnexion,name="logout"),
   
   
]
