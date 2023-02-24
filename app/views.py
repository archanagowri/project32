from django.shortcuts import render

# Create your views here.


def usd(request):
    d={'data':'Hi hEllo GooDmoRning'}
    return render(request,'usd.html',d)