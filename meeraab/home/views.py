from django.shortcuts import render
from .forms import ContactUsForm
# Create your views here.
def homepage(request):
    context={

    }
    return render(request,"home/homepage.html", context)


def about(request):
    return render(request, "home/about.html")


def contact(request):
    form = ContactUsForm()
    # form.fields['ip_address'].initial = ip_address
    if request.POST:
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'پیام شما با موفقیت ارسال گردید.')
            # obj.ip_address = ip_address
            # obj.save()
            # return redirect('/')

    context ={
        "form" : form,
        }

    return render(request, "home/contact.html", context)


def faq(request):
    return render(request, "home/faq.html")
