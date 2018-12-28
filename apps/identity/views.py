from django.shortcuts import render

# Create your views here.

def identity(request):
    return render(request,'identity/identity.html')