from django.contrib import admin

from ecom.models import Categorie, Image, Produit

# Register your models here.
class ImageInline(admin.TabularInline):
    model = Image
    extra = 1  # Vous pouvez ajuster le nombre initial de formulaires inline à afficher

class ProduitAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


admin.site.register(Categorie)
admin.site.register(Produit, ProduitAdmin)