from django.contrib import admin
from django.urls import path
from home import views as Home
from profil import views as Profil

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.home, name='home'),
    path ('profil/', Profil.profil, name='profil')
]
