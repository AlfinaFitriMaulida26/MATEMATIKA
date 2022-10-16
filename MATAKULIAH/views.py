from django.shortcuts import render
from MATAKULIAH.models import Matakuliah

# Create your views here.

def matakuliah(request):

    context = {
        'materials': Matakuliah.objects.all()
    }    
    return render(request, 'indexmatakuliah.html', context)
