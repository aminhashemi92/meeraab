from django.urls import path
from .views import *

app_name = "dashboard"
urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('well/defwell', defwell, name='defwell'),
    path('well/welllist', welllist, name='welllist'),
    path('bill/chahbill', chahbill, name='chahbill'),
    path('bill/chahvandbill', chahvandbill, name='chahvandbill'),
    path('bill/abvandbill', abvandbill, name='abvandbill'),

    path('well/defwellphysical/<slug:slug>', defwellphysical, name='defwellphysical'),

    path('transaction/abvandToAbvand', abvandToAbvand, name='abvandToAbvand'),
    path('transaction/abvandToChahvand', abvandToChahvand, name='abvandToChahvand'),
    path('transaction/chahvandToAbvand', chahvandToAbvand, name='chahvandToAbvand'),
    path('transaction/chahvandToChah', chahvandToChah, name='chahvandToChah'),
    path('transaction/chahToChahvand', chahToChahvand, name='chahToChahvand'),
    path('transaction/transactionlist', transactionlist, name='transactionlist'),

    path('trade/addtrade', addtrade, name='addtrade'),
    path('trade/tradelist', tradelist, name='tradelist'),
    path('trade/tradeboard', tradeboard, name='tradeboard'),

    path('license/license', license, name='license'),

    path('license/licensing/', licensing, name='licensing'),
    path('license/licensing/<slug:slug>', licensing, name='licensing'),



]
