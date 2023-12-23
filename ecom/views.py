from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Q
from ecom.models import Categorie, Produit
from .forms import ProduitForm,ProduitUpdateForm,ImageFormSet
from django.contrib import messages

# Create your views here.

def get_categorie_by_nom(nom):
    try:
        categorie = Categorie.objects.get(nom__icontains=nom)
        # Do something with the category, e.g., return it or perform additional operations.
        return categorie
    except Categorie.DoesNotExist:
        # Handle the case where the category with the specified name does not exist.
        return None

def index_ecom(request):
    nomproduit = request.GET.get('nomproduit','')
    cat = request.GET.get('cat','')
    print("produit",nomproduit)
    print("categorie",cat)
    categoriesModel = Categorie.objects.all()

    if nomproduit:
        if cat:
            categorie = get_categorie_by_nom(cat)
            if categorie:
                produits = Produit.objects.filter(Q(nom__icontains=nomproduit) & Q(categories=categorie))
            else:
                produits = []
        else:
            produits = Produit.objects.filter(nom__icontains=nomproduit)
    elif cat:
        categorie = get_categorie_by_nom(cat)
        if categorie:
            produits = Produit.objects.filter(categories=categorie)
        else:
            produits = []
    else:
         produits = Produit.objects.all().prefetch_related('categories')
        
         
    return render(request,'ecom/pages/index.html',{"produits":produits,'nomproduit':nomproduit,'cat': cat,'categories':categoriesModel})


def add_produit(request):
    form = ProduitForm()
    if request.method == 'POST':
        form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            produit=form.save()
            messages.success(request,"Produit ajouté avec success")
            form=ProduitForm()
            return redirect("detail-produit",pk=produit.id)

    return render(request, 'ecom/pages/add-produit.html', {'form': form})

def detail_produit(request,pk):
    produit = get_object_or_404(Produit,id=pk)
    
    return render(request, 'ecom/pages/detail-produit.html',{"produit":produit})    

def update_produit(request, pk):
    produit = get_object_or_404(Produit, id=pk)
    produit_form = ProduitUpdateForm(instance=produit)
    image_formset = ImageFormSet(instance=produit)
    print("test update")
    
    if request.method == 'POST':
        print("test post")
        produit_form = ProduitUpdateForm(request.POST, instance=produit)
        image_formset = ImageFormSet(request.POST, request.FILES, instance=produit)

        if produit_form.is_valid() and image_formset.is_valid():
            print("form valid")
            produit = produit_form.save()
            image_formset.save()
            return redirect('detail-produit',pk=produit.id)

    
    return render(request, 'ecom/pages/update-produit.html', {'produit_form': produit_form, 'image_formset': image_formset, 'produit': produit})