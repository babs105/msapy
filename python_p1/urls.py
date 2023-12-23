from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from .views import home,index

urlpatterns = [
    path('',index,name="index"),
    path('home/',home,name="home"),
    path('accounts/',include('connexion.urls')),
    path('carburant/',include('carburant.urls')),
    path('ecom/',include('ecom.urls')),
    path('admin/',admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)