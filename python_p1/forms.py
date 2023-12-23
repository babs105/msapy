from django import forms
from django.forms import formset_factory
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Password",max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Confirme Password",max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model=User
        fields=['username','email','first_name','last_name','password1','password2']



class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Password",max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-control','autocomplete':'on'}))
    class Meta:
        model=User
        fields=['username','password']


class FactureForm(forms.Form):
    nom_client = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    type_facture = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))

class ArticleForm(forms.Form):
    nom = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'p-2 form-control'}))
    quantite = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    prix_unitaire = forms.DecimalField(max_digits=10, decimal_places=2,widget=forms.TextInput(attrs={'class': 'form-control'}))
    prixtotal = forms.DecimalField(max_digits=10, decimal_places=2,widget=forms.TextInput(attrs={'class': 'form-control'}))
    # )
FactureArticleFormSet = formset_factory(ArticleForm, extra=1, can_delete=False)