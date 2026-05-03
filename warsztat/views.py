from django.contrib import messages
from django.db.models import Q, Count
from django.shortcuts import render, redirect, get_object_or_404
from .models import Obraczka
from .forms import ObraczkaForm



def lista_obraczek(request):
    query = request.GET.get('szukaj')
    obraczki = Obraczka.objects.all()

    if query:
        obraczki = obraczki.filter(
            Q(surowiec__icontains=query) |
            Q(wlasciciel__imie_nazwisko__icontains=query)
        )


    liczba_zlecen = obraczki.count()

    return render(request, 'warsztat/lista.html', {
        'obraczki': obraczki,
        'liczba_zlecen': liczba_zlecen
    })


def dodaj_obraczke(request):
    if request.method == "POST":
        form = ObraczkaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Nowa obrączka została dodana do rejestru!")
            return redirect('lista_obraczek')
    else:
        form = ObraczkaForm()
    return render(request, 'warsztat/dodaj.html', {'form': form})


def usun_obraczke(request, pk):
    obraczka = get_object_or_404(Obraczka, pk=pk)
    if request.method == "POST":
        obraczka.delete()
        messages.warning(request, f"Obrączka {obraczka.surowiec} została usunięta.")
        return redirect('lista_obraczek')
    return render(request, 'warsztat/usun_potwierdzenie.html', {'obraczka': obraczka})


def edytuj_obraczke(request, pk):
    obraczka = get_object_or_404(Obraczka, pk=pk)
    if request.method == "POST":
        form = ObraczkaForm(request.POST, instance=obraczka)
        if form.is_valid():
            form.save()
            messages.success(request, f"Zmiany w obrączce {obraczka.surowiec} zapisane!")
            return redirect('lista_obraczek')
    else:
        form = ObraczkaForm(instance=obraczka)
    return render(request, 'warsztat/dodaj.html', {'form': form, 'edycja': True})