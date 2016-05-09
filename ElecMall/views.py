from django.shortcuts import render


def index(request):
    context = {'request.user':request.user}
    return render(request, 'ElecMall/index.html', context)
