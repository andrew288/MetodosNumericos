from django.shortcuts import render

# Create your views here.

#Vista para gauss seidel
def Gauss_seidel(request):
    context = {}
    return render(request, 'gauss-seidel.html', context)