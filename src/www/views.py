from django.shortcuts import render

def maintenance(request):
    return render(request, 'maintenance.html')

def base(request):
    return render(request, '_home.html')

def layout(request):
    return render(request, '_base.html')