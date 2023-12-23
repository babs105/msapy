from django.db import models

# Create your models here.
# Modèle de catégorie
class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self) :
        return self.nom


class Produit(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=20, decimal_places=0)
    categories = models.ManyToManyField(Categorie)
    

    def __str__(self) :
        return self.nom

class Image(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='produit/',null=True,blank=True,)    
    


