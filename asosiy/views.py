from django.http import HttpResponse

from django.shortcuts import render,redirect

from.models import *

def hamma_studentlar(sorov):
    content = {
        "studentlar": Student.objects.all()

    }
    return render(sorov, 'Studentlar.html',content)


def hamma_rejalar(sorov):
    content = {
        "rejalar": Reja.objects.all()

    }
    return render(sorov, 'Rejalar.html',content)


def bajarilmagan_r(sorov):
    content = {
        "rejalar": Reja.objects.filter(bajarilgan = False)

    }
    return render(sorov, 'Rejalar.html',content)


def uchinchi_kurs(sorov):
    content = {
        "studentlar": Student.objects.filter(kurs__gt = 2)

    }
    return render(sorov, 'Studentlar.html',content)

def reja_ochir(sorov,son):
    Reja.objects.filter(id = son).delete()
    return redirect('/rejalar/')

def yangi_reja(sorov):
    if sorov.method.POST:
        Reja.objects.create(
            nom = sorov.POST['n'],
            student = Student.objects.get(id = sorov.POST['s'])
        )
        return redirect('/rejalar/')