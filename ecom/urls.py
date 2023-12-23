from django.urls import path
from .views import add_produit,detail_produit,update_produit,index_ecom


urlpatterns = [
    path('',index_ecom,name="index"),
    path('add-produit/',add_produit,name="add-produit"),
    path('detail-produit/<int:pk>',detail_produit,name="detail-produit"),
    path('update-produit/<int:pk>',update_produit,name="update-produit"),
    # path('register/',register,name="register"),
    # path('profil/',profil,name="profil"), 
    # path('profil-management/',profil_management,name="profil-management"),
    # path('delete-account/',delete_account,name="delete-account"),          
    # path('deconnexion/',deconnexion,name="logout"),
   
]
