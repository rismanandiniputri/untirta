from django.shortcuts import render
from . models import Dosen, Staff, Mahasiswa
# Create your views here.
def Pascasarjana(request):
    dosen = Dosen.objects.all()
    staff = Staff.objects.all()
    mahasiswa = Mahasiswa.objects.all()

    context = {
        'dataDosen': dosen,
        'dataStaff': staff,
        'dataMahasiswa': mahasiswa,
    }
    return render(request, 'pascasarjana.html', context)