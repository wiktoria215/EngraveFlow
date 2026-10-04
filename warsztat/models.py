from django.db import models


class Klient(models.Model):
    imie_nazwisko = models.CharField(max_length=100)
    telefon = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    class Meta:
        verbose_name = "Klient"
        verbose_name_plural = "Klienci"

    def __str__(self):
        return self.imie_nazwisko

class Obraczka(models.Model):
    surowiec = models.CharField(max_length=20)
    srednica = models.DecimalField(max_digits=5, decimal_places=1)
    szerokosc = models.DecimalField(max_digits=5, decimal_places=1)
    waga = models.DecimalField(max_digits=5, decimal_places=1, default=0)
    wlasciciel = models.ForeignKey(Klient, on_delete=models.CASCADE, related_name='obraczki')

    ma_kamienie = models.BooleanField(default=False)

    def __str__(self):
        return f"Obrączka {self.surowiec}, {self.srednica} mm"

    class Meta:
        verbose_name = "Obrączka"
        verbose_name_plural = "Obrączki"

