from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.  default=True or 30.0     blank=True =>optionnel   null=True



#-------------------------------------------------------------------------------
class Cuve(models.Model):
    nom = models.CharField(max_length=50)
    quantite = models.DecimalField(max_digits=10,default=0.0,decimal_places=2)
    

    class Meta:
        verbose_name = "Cuve"
        verbose_name_plural = "Cuves"

    def __str__(self) :
        return self.nom   

# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------
class Station(models.Model):
    nom = models.CharField(max_length=20)
    adresse = models.CharField(max_length=40)
    cuves = models.ManyToManyField(Cuve,through="Rajout",related_name="station_rajout")

  
    class Meta:
        verbose_name="Station"
        verbose_name_plural="Stations"

    def __str__(self):
        return self.nom
 
# ---------------------------------------------------------------------------------       

class Vehicule(models.Model):
    immatricule = models.CharField(max_length=50)
    categorie = models.CharField(max_length=50)
    affectation= models.CharField(max_length=100,null=True)
    cuves = models.ManyToManyField(Cuve, through='RavitaillementCuve', related_name='vehicules_ravitaille_cuves')
    stations = models.ManyToManyField(Station, through='RavitaillementStation', related_name='vehicules_ravitaille_station')
    
    class Meta:
        verbose_name = "Vehicule"
        verbose_name_plural = "Vehicules"

    def __str__(self) :
        return self.immatricule
    


#--------------------------------------------------------------------------------
class RavitaillementCuve(models.Model):
    cuve = models.ForeignKey(Cuve, on_delete=models.CASCADE)
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    date_heure_ravitaillement = models.DateTimeField()
    quantite = models.DecimalField(max_digits=10,default=0.0,decimal_places=2)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    class Meta:
        verbose_name = "RavitaillementCuves"
        verbose_name_plural = "RavitaillementCuves"

    def __str__(self):
        return f"Ravitaillement {self.vehicule} de {self.quantite} depuis {self.cuve} le {self.date_heure_ravitaillement}"        

    def get_absolute_url(self):
        return reverse("updateravitaillement",kwargs={"my_id":self.pk})



#--------------------------------------------------------------------------------
class RavitaillementStation(models.Model):
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    date_heure_ravitaillement = models.DateTimeField()
    quantite = models.DecimalField(max_digits=10,default=0.0,decimal_places=2)
    

    class Meta:
        verbose_name = "RavitaillementStations"
        verbose_name_plural = "RavitaillementStations"

    def __str__(self):
        return f"Ravitaillement {self.vehicule} de {self.quantite} a la {self.station} le {self.date_heure_ravitaillement}"        

    # def get_absolute_url(self):
    #     return reverse("updateravitaillement",kwargs={"my_id":self.pk})



#------------------------------------------------------------------------------------

class Rajout(models.Model):
    station = models.ForeignKey(Station,on_delete=models.CASCADE)
    cuve = models.ForeignKey(Cuve,on_delete=models.CASCADE)
    date_heure_rajout= models.DateTimeField()
    quantite_rajout=models.DecimalField(max_digits=10,default=0.0,decimal_places=2)

    class Meta:
        verbose_name="Rajout"
        verbose_name_plural="Rajouts"

    def __str__(self):
        return f"Rajout {self.cuve} de {self.quantite_rajout} depuis la  {self.station} le {self.date_heure_rajout}"







#         from datetime import datetime
# from django.utils import timezone

# # Supposons que vous avez déjà des instances de CuveCarburant et Vehicule
# cuve = CuveCarburant.objects.get(pk=1)
# vehicule = Vehicule.objects.get(pk=1)

# # Ajouter la relation many-to-many avec la date et l'heure de ravitaillement
# date_heure_ravitaillement = datetime(2023, 3, 12, 20, 34)
# ravitaillement = Ravitaillement.objects.create(cuve=cuve, vehicule=vehicule, date_heure_ravitaillement=date_heure_ravitaillement)

# # Ajouter la relation many-to-many à travers la table intermédiaire
# cuve.vehicules.add(vehicule, through_defaults={'date_heure_ravitaillement': date_heure_ravitaillement})
