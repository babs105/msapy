from django.urls import path
from .views import addravitaillement, delravitaillement, home, listrajout,listcuve ,update_ravitaillement
from .views import liststation,listvehicule,listravitaillementcuve,listravitaillementstation

urlpatterns = [
    path('',home,name="carburant-home"),
    path("addravitaillement/",addravitaillement,name="addravitaillement"),
    path('listravitaillementcuve/',listravitaillementcuve,name="listravitaillementcuve"),
    path('updateravitaillement/<int:my_id>',update_ravitaillement,name="updateravitaillement"),
    path('delravitaillement/<int:my_id>',delravitaillement,name="delravitaillement"),



    path('listrajout/',listrajout,name="listrajout"),
    path('listcuve/',listcuve,name="listcuve"),
    path('listvehicule/',listvehicule,name="listvehicule"),
    path('liststation/',liststation,name="liststation"),
    path('listravitaillementstation/',listravitaillementstation,name="listravitaillementstation"),
]
