from django.shortcuts import render

def profil(request):
    context = {
        'kata': 'Ini Halaman Profile'
    }
    return render(request, 'index.html', context)
