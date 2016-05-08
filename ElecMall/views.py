from django.shortcuts import render


from account.decorators import login_required


def index(request):
    return render(request, 'ElecMall/index.html')
