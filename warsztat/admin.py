from django.contrib import admin
from .models import Klient, Obraczka

admin.site.register((Klient))
admin.site.register(Obraczka)
# Register your models here.
