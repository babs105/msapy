from django import forms
from django.forms import formset_factory
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile



# -------------------------------------------
class UserForm(UserCreationForm):
    # username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}),error_messages={'required': 'Nom utilisateur est obligatoire'} )
    username = forms.CharField(label="Nom Utilisateur",max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}),error_messages={'required': 'Nom utilisateur est obligatoire'} )
    email = forms.CharField(label="Email",max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label="Prénom",max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="Nom",max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Mot de Passe",max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Confirmer Mot de Passe",max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model=User
        fields=['username','email','first_name','last_name','password1','password2']


# -------------------------------------------
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Nom Utilisateur",max_length=100,widget=forms.TextInput(attrs={'class': 'form-control','autocomplete': 'current-password'}))
    password = forms.CharField(label="Mot de Passe",max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-control','autocomplete': 'current-password'}))
    class Meta:
        model=User
        fields=['username','password']
    
    def clean_username(self,*arg,**kwrgs):
            username=self.cleaned_data.get('username')
            if not username:
                self.fields['username'].widget.attrs['class'] += 'is-invalid'  # Ajoutez une classe 'error'
                raise forms.ValidationError('Nom utilisateur est obligatoire', code='empty_username')
            # elif not 'msa'in username:
            #     self.fields['username'].widget.attrs['class'] += ' is-invalid'  # Ajoutez une classe 'error'
            #     raise forms.ValidationError('Nom utilisateur doit contenir la sous-chaîne "msa"', code='invalid_username')  
            else:
                return username



    # def clean_username(self, *args, **kwargs):
    #     username = self.cleaned_data.get('username')
    
    #     if not username or 'msa' not in username:
    #         self.fields['username'].widget.attrs['class'] += ' is-invalid'  # Ajoutez une classe 'error'
        
    #         if not username:
    #                 raise forms.ValidationError('Nom utilisateur est obligatoire', code='empty_username')
    #         else:
    #                 raise forms.ValidationError('Nom utilisateur doit contenir la sous-chaîne "msa"', code='invalid_username')
    #     return username




# -------------------------------------------
class UpdateProfileForm(forms.ModelForm):
    
    profile_pic = forms.ImageField(label="Photo profil",widget=forms.FileInput(attrs={'class':'form-control-file'}))
    
    class Meta:
        model = Profile
        fields=['profile_pic',]


# -------------------------------------------
class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(label="Nom Utilisateur",max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}),error_messages={'required': 'Nom utilisateur est obligatoire'} )
    email = forms.CharField(label="Email",max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    password=None
    
    class Meta:
        model=User
        fields=['username','email',]
        exclude=['password1','password2',]

# -------------------------------------------





# -------------------------------------------
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