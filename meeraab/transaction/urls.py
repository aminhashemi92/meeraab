from django.urls import path
from .views import *

app_name = "transaction"
urlpatterns = [
    path('ajax/load-chahbill/', load_chahbill, name='ajax_load_chahbill'),
    path('ajax/load-chahvandbill/', load_chahvandbill, name='ajax_load_chahvandbill'),
    path('ajax/load-abvandbill/', load_abvandbill, name='ajax_load_abvandbill'),


    path('ajax/load-chahcredit/', load_chahcredit, name='ajax_load_chahcredit'),
    # path('', homepage, name='homepage'),
    # path('about', about, name='about'),
    # path('contact', contact, name='contact'),
    # path('faq', faq, name='faq'),
]
