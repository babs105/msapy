# views.py
from django.shortcuts import render,redirect
from .forms import FactureArticleFormSet, UpdateUserForm,UserForm,UserLoginForm,UpdateProfileForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . models import Profile

def register(request):
    form=UserForm()
    if request.method=='POST':
        form=UserForm(data=request.POST)
        if form.is_valid():

            current_user = form.save(commit=False)
           
            form.save()
            profile = Profile.objects.create(user=current_user)

            messages.success(request,"Votre compte a été créé")
            return redirect('login')
        else:
            messages.error(request,form.errors)
    return render(request,'connexion/pages/register.html',{"form":form})

def connexion(request):
    form = UserLoginForm()
    next = request.GET.get("next")
    if request.method =='POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            data=form.cleaned_data
            user= authenticate(request,username=data.get("username"),password=data.get("password"))
            if user is not None and user.is_active: 
                login(request,user)
                if next:
                    return redirect(next) 
                   
                else:
                    messages.success(request,"Bienvenue")
                    return redirect("home")
            else:
                messages.error(request,"Votre compte a un souci ")     
    return render(request,'connexion/pages/login.html',{"form":form})

@login_required
def deconnexion(request):
   if request.user.is_authenticated:
      logout(request)
      messages.success(request, "Vous avez été déconnecté avec succès.")
      return redirect('index')


@login_required
def profil(request):
    current_user = request.user
    profile = Profile.objects.get(user = current_user)
    

    return render(request,'connexion/pages/profil.html',{"profile":profile})

@login_required
def profil_management(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)

    form_user = UpdateUserForm(instance=current_user)
    form_profile = UpdateProfileForm(instance=profile)
    

    if request.method =='POST':
        form_user = UpdateUserForm(request.POST,instance=current_user)
        form_profile = UpdateProfileForm(request.POST,request.FILES,instance=profile)
        if form_user.is_valid():
            form_user.save()
            messages.success(request,"Votre profile a été modifié")
            return redirect('profil')

        if form_profile.is_valid():
            form_profile.save()
            messages.success(request,"Votre profile a été modifié")
            return redirect('profil')

    return render(request,'connexion/pages/profil-management.html',{'form_user':form_user,'form_profile':form_profile})


@login_required
def delete_account(request):
    current_user = request.user
    if request.method =='POST':
        current_user.delete()
        messages.success(request,"Votre compte a été supprimé")
        return redirect('index')
    return render(request,'connexion/pages/delete-account.html')