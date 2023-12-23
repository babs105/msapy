from datetime import datetime,timedelta
from django.utils import timezone
from django.db.models import Q
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Cuve, Rajout, RavitaillementCuve,RavitaillementStation, Station, Vehicule
from .forms import RavitaillementForm
from django.contrib import messages
from django.db import IntegrityError, transaction
import logging

logger = logging.getLogger(__name__)

# Create your views here.
@login_required
def home(request):
    return render(request, 'carburant/pages/index.html')

# form = RowProductForm(request.POST, request.FILES)

@login_required
def addravitaillement(request):
    form = RavitaillementForm()
    if request.method == "POST":
        form = RavitaillementForm(data=request.POST or None)
        if form.is_valid():
            try:
                with transaction.atomic():
                    data = form.cleaned_data
                    cuve = data.get("cuve")
                    quantiteRavitaillee = data.get("quantite")

                    ravitaillement = form.save(commit=False)
                    ravitaillement.user = request.user

                    cuve.quantite -= quantiteRavitaillee
                    ravitaillement.save() 
                    cuve.save()
                    form = RavitaillementForm()
                    messages.success(request, "Ajout Ravitaillement")
                    return redirect('addravitaillement')  # Redirige vers la vue d'ajout de ravitaillement
            except IntegrityError:
                messages.error(request, "Erreur d'intégrité lors de l'ajout de la relation many-to-many.")
            except Exception as e:
                messages.error(request, f"Une erreur s'est produite : {e}")
            # return redirect('login')
    return render(request, 'carburant/pages/ravitaillement_cuve/addravitaillement.html',{"form":form})


@login_required
def listravitaillementcuve(request):
    keyword = request.GET.get('keyword','')
    keyword_date = request.GET.get('keyword_date','')
    # Récupérer le numéro de la page demandée
    page = request.GET.get('page')
   
    if keyword_date:
        try:
            keyword_date = datetime.strptime(keyword_date, '%Y-%m-%d')
            # Calcul de la plage de dates pour la journée entière
            start_of_day = timezone.make_aware(keyword_date.replace(hour=0, minute=0, second=0))
            end_of_day = start_of_day + timedelta(days=1)
        except ValueError:
            logger.error(f"Invalid date format: {keyword_date}")
            start_of_day = None
            end_of_day = None

    # if  keyword :
    #     ravitaillements = RavitaillementCuve.objects.all().select_related(
    #             'vehicule','cuve').order_by('-date_heure_ravitaillement').filter( 
    #         Q(vehicule__immatricule__icontains = keyword)| 
    #         Q(vehicule__affectation__icontains = keyword)| 
    #         Q(cuve__nom__icontains = keyword))
    # elif keyword_date:
    #         ravitaillements = RavitaillementCuve.objects.all().select_related(
    #         'vehicule','cuve').order_by('-date_heure_ravitaillement'
    #         ).filter(date_heure_ravitaillement__range = (start_of_day,end_of_day))

    # elif keyword and keyword_date :

    #         ravitaillements = RavitaillementCuve.objects.all().select_related(
    #             'vehicule','cuve').order_by('-date_heure_ravitaillement').filter( 
    #         Q(vehicule__immatricule__icontains = keyword)| 
    #         Q(vehicule__affectation__icontains = keyword)| 
    #         Q(cuve__nom__icontains = keyword)&
    #         Q(date_heure_ravitaillement__range = (start_of_day,end_of_day))
    #             )     
    # else:   
    #     ravitaillements = RavitaillementCuve.objects.all().select_related('vehicule','cuve').order_by('-date_heure_ravitaillement')
        # current_user=request.user
        # ravitaillements=RavitaillementCuve.objects.all().select_related('vehicule','cuve').filter(user=current_user)
        # ravitaillements=RavitaillementCuve.objects.all().select_related('vehicule','cuve').filter(cuve__nom="CUVE MOBILE")
        # ravitaillements=RavitaillementCuve.objects.all().filter(cuve__nom="CUVE MOBILE")
        # ravitaillements=RavitaillementCuve.objects.all().filter(cuve__nom="CUVE MOBILE")
    if keyword_date:
        if keyword:
            ravitaillements = RavitaillementCuve.objects.all().select_related(
                'vehicule','cuve').order_by('-date_heure_ravitaillement').filter( 
            Q(vehicule__immatricule__icontains = keyword)| 
            Q(vehicule__affectation__icontains = keyword)| 
            Q(cuve__nom__icontains = keyword)&
            Q(date_heure_ravitaillement__range = (start_of_day,end_of_day)))
        else:
            ravitaillements = RavitaillementCuve.objects.all().select_related(
            'vehicule','cuve').order_by('-date_heure_ravitaillement'
            ).filter(date_heure_ravitaillement__range = (start_of_day,end_of_day))
    elif keyword:
            ravitaillements = RavitaillementCuve.objects.all().select_related(
                'vehicule','cuve').order_by('-date_heure_ravitaillement').filter( 
            Q(vehicule__immatricule__icontains = keyword)| 
            Q(vehicule__affectation__icontains = keyword)| 
            Q(cuve__nom__icontains = keyword))
    else:
         ravitaillements = RavitaillementCuve.objects.all().select_related('vehicule','cuve').order_by('-date_heure_ravitaillement')



    # Nombre d'éléments par page
    elements_par_page = 10
    paginator = Paginator(ravitaillements, elements_par_page)



    try:
        ravitaillements_page = paginator.page(page)
    except PageNotAnInteger:
        # Si le paramètre page n'est pas un entier, afficher la première page
        ravitaillements_page = paginator.page(1)
    except EmptyPage:
        # Si la page est hors de portée (par exemple, 9999), afficher la dernière page
        ravitaillements_page = paginator.page(paginator.num_pages)

    return render(request, 'carburant/pages/ravitaillement_cuve/listravitaillementcuve.html',
    {
    "ravitaillements_page":ravitaillements_page,
    "keyword":keyword,
    "keyword_date":keyword_date
    })


@login_required
def listravitaillementstation(request):
    ravitaillements = RavitaillementStation.objects.all().select_related('vehicule','station').order_by('-date_heure_ravitaillement')
    
    return render(request, 'carburant/pages/ravitaillement_station/listravitaillementstation.html',{"ravitaillements":ravitaillements})




@login_required
def listcuve(request):
    cuves = Cuve.objects.all()
    
    return render(request, 'carburant/pages/cuve/listcuve.html',{"cuves":cuves})



@login_required
@transaction.atomic()
def update_ravitaillement(request,my_id):
    old_ravi = get_object_or_404(RavitaillementCuve,id=my_id)
    # old_ravi = Ravitaillement.objects.get(id=my_id)
    formatted_date = old_ravi.date_heure_ravitaillement.strftime('%Y-%m-%dT%H:%M')
    oldcuve=old_ravi.cuve
    oldqteravi=old_ravi.quantite
# Passez la date formatée au formulaire

    form = RavitaillementForm(initial={'date_heure_ravitaillement': formatted_date},instance=old_ravi)
    if request.method == "POST":
        form = RavitaillementForm(request.POST,instance=old_ravi)
        if form.is_valid():
                data = form.cleaned_data
                print(old_ravi.cuve)
                newcuve = data.get("cuve")
                newqteravi = data.get("quantite")

                ravitaillement = form.save(commit=False)
                ravitaillement.user = request.user

                if newcuve.id == oldcuve.id:
                    print("#####  n=o        ###########")
                    oldRavitaillements  =  oldcuve.ravitaillementcuve_set.all()
                    for oldravitaillement in oldRavitaillements:
                        if oldravitaillement.id == form.instance.id:
                            qte_amodifier =  newqteravi - oldravitaillement.quantite

                            if(qte_amodifier > 0):
                              newcuve.quantite -= qte_amodifier

                            else:
                              newcuve.quantite += abs(qte_amodifier)
                            break
                    
                    ravitaillement.save()  # Maintenant, sauvegarde l'objet Ravitaillement avec les données associées
                    newcuve.save()
                else:
                    print("################")
                    oldcuve.quantite += oldqteravi
                    newcuve.quantite -= newqteravi

                    print(oldcuve.quantite)
                    print(newcuve.quantite)
                    print("################")

                    ravitaillement.save()
                    oldcuve.save()
                    newcuve.save()
                    
                    
                form = RavitaillementForm()
                messages.success(request, "Modification Ravitaillement Reussi")
    return render(request, 'carburant/pages/ravitaillement_cuve/updateravitaillement.html',{"form":form})

@login_required
def delravitaillement(request,my_id):
    obj = get_object_or_404(RavitaillementCuve,id=my_id)
    context={
        "vehicule" : obj.vehicule,
        "quantite" :obj.quantite,
        "date" : obj.date_heure_ravitaillement,
    } 
    print("######## delll########")
    
    if request.method =='POST' : 
        obj.delete()
        messages.success(request, "Ravitaillement Supprimé")
        return redirect('listravitaillement')
    return render(request,'carburant/pages/ravitaillement_cuve/delravitaillement.html',context)


@login_required
def listrajout(request):
    rajouts = Rajout.objects.all().select_related('station','cuve').order_by('-date_heure_rajout')
    
    return render(request, 'carburant/pages/rajout/listrajout.html',{"rajouts":rajouts})




@login_required
def liststation(request):
    stations = Station.objects.all()
    
    return render(request, 'carburant/pages/station/liststation.html',{"stations":stations})

@login_required
def listvehicule(request):
    vehicules = Vehicule.objects.all().order_by('immatricule')
    
    return render(request, 'carburant/pages/vehicule/listvehicule.html',{"vehicules":vehicules})