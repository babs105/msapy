from django import forms
from .models import Categorie, Produit,Image
from django.forms import ClearableFileInput, FileField 
from django.core.validators import validate_image_file_extension
import imghdr

# -----------------------------------------------------------------------
class MultipleFileInput(ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(FileField):
    default_validators = [validate_image_file_extension]
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

# class MultipleFileInput(ClearableFileInput):
#     def __init__(self, attrs=None):
#         attrs = {'multiple': True}
#         super().__init__(attrs)

# -----------------------------------------------------------------------
class ProduitForm(forms.ModelForm):
    nom = forms.CharField(label="Nom Produit",max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}) )
    description = forms.CharField(label="Description",max_length=100,widget=forms.Textarea(attrs={'class': 'form-control'}))
    prix = forms.DecimalField(label="Prix",widget=forms.NumberInput(attrs={'class': 'form-control','min': 0, 'step': 'any'}))
    # images = forms.ImageField(label="Images",widget=forms.ClearableFileInput(attrs={"allow_multiple_selected": True}), required=False)
    categories=forms.ModelMultipleChoiceField(queryset=Categorie.objects.all(),widget=forms.CheckboxSelectMultiple())
    images= MultipleFileField()
    # images = forms.FileField(widget=MultipleFileInput(), required=False)

    class Meta:
        model = Produit
        fields = ['nom', 'description','prix','categories']

    def save(self, commit=True):
        produit = super().save(commit)
        
        # Enregistrez les images associées au produit
        for image in self.files.getlist('images'):
            Image.objects.create(produit=produit, image=image)

        return produit


    def clean_images(self):
        images = self.cleaned_data.get('images')
        if images:
            for i, image in enumerate(images, start=1):
                # Vérifier le type de fichier en utilisant imghdr
                file_type = imghdr.what(image)

                if file_type not in ['jpeg', 'png', 'gif']:
                    self.add_error(f'images', "Seules les images (jpeg, png, gif) sont autorisées.")

                    # Assurez-vous que la clé 'class' existe avant de l'utiliser
                    if 'class' in self.fields['images'].widget.attrs:
                        self.fields['images'].widget.attrs['class'] += ' is-invalid'
                    else:
                        self.fields['images'].widget.attrs['class'] = 'is-invalid'

                    return images

        return images   



# ------------ update ---------- update ---------- update ----------- ------------
class ProduitUpdateForm(forms.ModelForm):
    nom = forms.CharField(label="Nom Produit", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label="Description", max_length=100, widget=forms.Textarea(attrs={'class': 'form-control'}))
    prix = forms.DecimalField(label="Prix", widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'step': 'any'}))
    categories=forms.ModelMultipleChoiceField(
        queryset=Categorie.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )
    class Meta:
        model = Produit
        fields = ['nom', 'description', 'prix','categories']

class ImageForm(forms.ModelForm):
    # image = forms.ImageField(label="Photo profil",widget=forms.FileInput(attrs={'class':'form-control-file'}))
    class Meta:
        model = Image
        fields = ['image']

ImageFormSet = forms.inlineformset_factory(Produit, Image, form=ImageForm, extra=1, can_delete=True)