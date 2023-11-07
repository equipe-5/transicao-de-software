from django.shortcuts import render

def home(request):
    return render(request, 'cliente/pages/home.html', context={
        'name': 'Geovana Hecke'
    })