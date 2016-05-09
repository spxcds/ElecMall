from __future__ import unicode_literals
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from account.models import Customer

def index(request):
    try:
        user_id = request.session.get("user_id", None)
        request.user = Customer.objects.get(id=user_id)
    except Customer.DoesNotExist:
        pass
    return render(request, 'ElecMall/index.html')
