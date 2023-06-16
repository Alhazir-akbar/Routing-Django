from django.shortcuts import render

def home(request):
    context = {
        'kata' : 'Halaman Home'
    }
    return render(request, 'index.html', context)


