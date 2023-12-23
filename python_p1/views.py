# views.py
from django.shortcuts import render,redirect

from connexion.models import Profile
from .forms import FactureForm, FactureArticleFormSet,UserForm,UserLoginForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    return render(request,'homeapp/pages/index.html')


@login_required
def home(request):
    return render(request,'homeapp/pages/home.html')

# @login_required
# def profil(request):

#     profile = Profile.objects.get(user = request.user)

#     return render(request,'pages/profil.html',{'profile':profile})





# def register(request):
#     form=UserForm()
#     if request.method=='POST':
#         form=UserForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request,"Votre compte a ete cree")
#             return redirect('login')
#         else:
#             messages.error(request,form.errors)
#     return render(request,'accounts/register.html',{"form":form})

# def connexion(request):
#     form = UserLoginForm()
#     if request.method =='POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             data=form.cleaned_data
#             user= authenticate(request,username=data.get("username"),password=data.get("password"))
#             if user is not None and user.is_active:
#                 login(request,user)
#                 messages.success(request,"Bienvenue")
#                 return redirect("home")
#         else:
#             messages.error(request,"Erreur d'Authentification")
#     return render(request,'accounts/login.html',{"form":form})

# @login_required
# def deconnexion(request):
#     logout(request)
#     return redirect('login')



# @login_required
# def ajout_facture(request):
#     if request.method == 'POST':
#         facture_form = FactureForm(request.POST, prefix='facture')
#         formset = FactureArticleFormSet(request.POST, prefix='articles')
#         if facture_form.is_valid() and formset.is_valid():
#             # Traitez les données du formulaire ici
#             nom_client = facture_form.cleaned_data.get('nom_client')
#             type_facture = facture_form.cleaned_data['type_facture']

#             print(nom_client)

#             print(type_facture)
#             print(formset.cleaned_data)
#             facture_form = FactureForm(prefix='facture')
#             formset = FactureArticleFormSet(prefix='articles')
#             # for form in formset:
#             #     nom_article = form.cleaned_data
#                 # quantite = form.cleaned_data['quantite']
#                 # prix_unitaire = form.cleaned_data['prix_unitaire']
#                 # prixtotal = form.cleaned_data['prixtotal']
                
#                 # Faites quelque chose avec chaque article
                
#             # Redirigez ou effectuez toute autre action nécessaire après la soumission réussie
#     else:
#         facture_form = FactureForm(prefix='facture')
#         formset = FactureArticleFormSet(prefix='articles')

#     return render(request, 'pages/ajout_facture.html', {'facture_form': facture_form, 'formset': formset})
