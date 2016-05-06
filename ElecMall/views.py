from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'ElecMall/index1.html', context)
