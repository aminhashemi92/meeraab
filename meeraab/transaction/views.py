from django.shortcuts import render
from django.db.models import Q
from .models import *
from well.models import *
# Create your views here.
def load_chahbill(request):
    accountID = request.GET.get('accountID')
    chah = Chah.objects.get(accountID=accountID)
    transactions = Transaction.objects.filter(Q(from_well=chah) | Q(to_well=chah))
    # states = State.objects.filter(country_id=country_id).order_by('name')
    context ={'transactions':transactions,'accountID':accountID,}
    return render(request, 'transaction/listchahbill.html',context)

def load_chahcredit(request):
    accountID = request.GET.get('accountID')
    chah = Chah.objects.get(accountID=accountID)
    credits = Credit.objects.filter(well=chah)
    buckets = credits.values_list('bucket', flat=True).distinct()
    queryset = []
    for bucket in buckets:
        c = credits.filter(bucket=bucket).last()
        cd = {'bucket':c.bucket.name, 'credit':c.credit,'created':c.created}
        queryset.append(cd)

    context ={'queryset':queryset,'accountID':accountID,}
    return render(request, 'transaction/listchahcredit.html',context)


def load_chahvandbill(request):
    accountID = request.GET.get('accountID')
    chahvand = ChahVand.objects.get(accountID=accountID)
    transactions = Transaction.objects.filter(Q(from_chahvand=chahvand) | Q(to_chahvand=chahvand))
    # states = State.objects.filter(country_id=country_id).order_by('name')
    context ={'transactions':transactions,'accountID':accountID,}
    return render(request, 'transaction/listchahvandbill.html',context)


def load_abvandbill(request):
    accountID = request.GET.get('accountID')
    abvand = AbVand.objects.get(accountID=accountID)
    transactions = Transaction.objects.filter(Q(from_abvand=abvand) | Q(to_abvand=abvand))
    # states = State.objects.filter(country_id=country_id).order_by('name')
    context ={'transactions':transactions, 'accountID':accountID,}
    return render(request, 'transaction/listabvandbill.html',context)
