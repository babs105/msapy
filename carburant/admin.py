from django.contrib import admin

from .models import Rajout, RavitaillementStation, Station, Vehicule,Cuve,RavitaillementCuve

# Register your models here.

class AdminVehicule(admin.ModelAdmin):
    list_display = ('immatricule', 'categorie','affectation')  
    # list_editable = ("categorie", )
    search_fields = ("immatricule", "affectation", )
    list_filter = ("categorie", )

class AdminCuve(admin.ModelAdmin):
    list_display = ('nom', 'quantite',)  
    # list_editable = ("categorie", )
    # search_fields = ("immatricule", "affectation", )
    # list_filter = ("categorie", )   

class AdminRavitaillementCuve(admin.ModelAdmin):
    list_display = ('date_heure_ravitaillement','vehicule' ,'quantite','cuve')  
 
    def save_model(self, request, obj, form, change):
        oldravi=RavitaillementCuve.objects.get(pk=obj.pk)
        oldcuve=oldravi.cuve
        newcuve=obj.cuve
        if not change:
            newcuve.quantite -= obj.quantite
            newcuve.save()
            obj.save()
        else:
            if newcuve.id == oldcuve.id: # meme cuve il va falloir retrouver le ravitailllement a modifier
                    print("#####  n=o        ###########")
                    ravis_cuve  =  newcuve.ravitaillementcuve_set.all()
                    for r in ravis_cuve:
                        if r.id == obj.id:
                            qte_amodifier =  obj.quantite - r.quantite

                            if(qte_amodifier > 0):
                              newcuve.quantite -= qte_amodifier

                            else:
                              newcuve.quantite += abs(qte_amodifier)
                            break
                    
                    obj.save()  # Maintenant, sauvegarde l'objet Ravitaillement avec les données associées
                    newcuve.save()
            else:
                    print("################")
                    oldcuve.quantite += oldravi.quantite
                    newcuve.quantite -= obj.quantite

                    obj.save()
                    oldcuve.save()
                    newcuve.save()



class AdminRavitaillementStation(admin.ModelAdmin):
    list_display = ('date_heure_ravitaillement','vehicule' ,'quantite','station')  


class AdminStation(admin.ModelAdmin):
    list_display = ('nom', 'adresse',)


class AdminRajout(admin.ModelAdmin):
    list_display = ('date_heure_rajout','station' ,'quantite_rajout','cuve')  




admin.site.register(Vehicule,AdminVehicule)        
admin.site.register(Cuve,AdminCuve)               
admin.site.register(RavitaillementCuve,AdminRavitaillementCuve)   
admin.site.register(RavitaillementStation,AdminRavitaillementStation) 
admin.site.register(Rajout,AdminRajout)  
admin.site.register(Station,AdminStation)  