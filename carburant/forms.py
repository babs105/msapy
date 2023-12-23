from django import forms
from .models import Cuve, RavitaillementCuve, Vehicule





# -----------------------------------------------------------------------
class RavitaillementForm(forms.ModelForm):
    date_heure_ravitaillement = forms.DateTimeField(
        widget=forms.DateTimeInput(
         attrs={'type': 'datetime-local','class': 'form-control'}),input_formats=['%Y-%m-%dT%H:%M'])
    vehicule = forms.ModelChoiceField(queryset=Vehicule.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    cuve = forms.ModelChoiceField(queryset=Cuve.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    quantite = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control','min': 0, 'step': 'any'}))

    class Meta:
        model=RavitaillementCuve
        fields=['date_heure_ravitaillement','vehicule','cuve','quantite']
    
    # def as_custom_p(self):
    #     """Rend le formulaire avec un champ de date personnalisé."""
    #     custom_date_input = self['date_heure_ravitaillement'].as_widget(attrs={'type': 'datetime-local', 'class': 'form-control'})
    #     return mark_safe(f'<p>Date et Heure Ravitaillement : {custom_date_input}</p>')