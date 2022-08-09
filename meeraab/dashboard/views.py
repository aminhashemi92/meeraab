from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from transaction.forms import *
from transaction.models import *
from django.contrib import messages
from django.forms import formset_factory, BaseFormSet
from well.forms import *
from transaction.models import *
from trading.models import *
from trading.forms import *
from license.forms import *
# Create your views here.



@login_required
def dashboard(request):
    well_count = Well.objects.all().count()
    user_count = User.objects.all().count()
    trade_count = Trade.objects.all().count()
    trans_count = Transaction.objects.all().count()
    context={
        'well_count':well_count,
        'user_count':user_count,
        'trade_count':trade_count,
        'trans_count':trans_count,
    }
    return render(request, "dashboard/dashboard.html", context)

@login_required
def abvandToAbvand(request):
    form = AbvandToAbvandTransactionForm()
    if request.POST:
        form = AbvandToAbvandTransactionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'اطلاعات شما با موفقیت ثبت گردید')
            # return redirect('dashboard:transactionlist')
    context={'form':form,}
    return render(request, "dashboard/abvandToAbvand.html", context)


@login_required
def abvandToChahvand(request):
    form = AbvandToChahvandTransactionForm()
    if request.POST:
        form = AbvandToChahvandTransactionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'اطلاعات شما با موفقیت ثبت گردید')
            # return redirect('dashboard:transactionlist')
    context={'form':form,}
    return render(request, "dashboard/abvandToChahvand.html", context)


@login_required
def chahvandToAbvand(request):
    form = ChahvandToAbvandTransactionForm()
    if request.POST:
        form = ChahvandToAbvandTransactionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'اطلاعات شما با موفقیت ثبت گردید')
            # return redirect('dashboard:transactionlist')
    context={'form':form,}
    return render(request, "dashboard/chahvandToAbvand.html", context)


@login_required
def chahToChahvand(request):
    form = ChahToChahvandTransactionForm()
    if request.POST:
        form = ChahToChahvandTransactionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'اطلاعات شما با موفقیت ثبت گردید')
            # return redirect('dashboard:transactionlist')
    context={'form':form,}
    return render(request, "dashboard/chahToChahvand.html", context)


@login_required
def chahvandToChah(request):
    form = ChahvandToChahTransactionForm()
    if request.POST:
        form = ChahvandToChahTransactionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'اطلاعات شما با موفقیت ثبت گردید')
            # return redirect('dashboard:transactionlist')
    context={'form':form,}
    return render(request, "dashboard/chahvandToChah.html", context)


@login_required
def transactionlist(request):
    # form = ChahvandToChahTransactionForm()
    transactions = Transaction.objects.all()
    context={'transactions':transactions,}
    return render(request, "dashboard/transactionlist.html", context)


@login_required
def defwell(request):
    # form = ChahvandToChahTransactionForm()
    form = WellForm()
    if request.POST:
        form = WellForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            messages.success(request,'اطلاعات چاه ثبت گردید، اطلاعات فیزیکی چاه را وارد کنید')

            return redirect('dashboard:defwellphysical', slug=obj.slug)
    context={'form':form,}
    return render(request, "dashboard/defwell.html", context)

@login_required
def defwellphysical(request, slug):
    well = Well.objects.get(slug=slug)
    wellphysical = WellPhysicalInfo.objects.get(well=well)
    form = WellPhysicalInfoForm(instance = wellphysical)
    if request.POST:
        form = WellPhysicalInfoForm(request.POST, request.FILES, instance = wellphysical)
        if form.is_valid():
            form.save()
            messages.success(request,'اطلاعات فیزیکی چاه ثبت گردید.')

    context={'form':form,}
    return render(request, "dashboard/defwellphysical.html", context)


@login_required
def welllist(request):
    wells = Well.objects.all()
    context={
    "wells": wells,
    }
    return render(request,"dashboard/welllist.html", context)


@login_required
def chahbill(request):
    chahbills = Chah.objects.filter(status=True)
    context={
        'chahbills':chahbills,
        }
    return render(request,"dashboard/chahbill.html", context)

@login_required
def chahvandbill(request):
    chahbills = ChahVand.objects.filter(status=True)
    context={
        'chahbills':chahbills,
        }
    return render(request,"dashboard/chahvandbill.html", context)

@login_required
def abvandbill(request):
    chahbills = AbVand.objects.filter(status=True)
    context={
        'chahbills':chahbills,
        }
    return render(request,"dashboard/abvandbill.html", context)



@login_required
def addtrade(request):
    form = TradeForm()
    if request.POST:
        form = TradeForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.creator = request.user
            obj.save()
            messages.success(request,'اطلاعات با موفقیت ثبت گردید')
            return redirect('dashboard:addtrade')

    context={
        'form':form,
        }
    return render(request,"dashboard/addtrade.html", context)


@login_required
def tradelist(request):
    tradelist = Trade.objects.all()
    context={
        'tradelist':tradelist,
        }
    return render(request,"dashboard/tradelist.html", context)


@login_required
def tradeboard(request):
    tradelist = Trade.objects.filter(status=True)
    context={
        'tradelist':tradelist,

        }
    return render(request,"dashboard/tradeboard.html", context)


@login_required
def license(request):
    wells = Well.objects.all()
    context={
        'wells':wells,
        }
    return render(request,"dashboard/license.html", context)

class RequiredFormSet(BaseFormSet):
    def __init__(self, *args, **kwargs):
        super(RequiredFormSet, self).__init__(*args, **kwargs)
        for form in self.forms:
            form.empty_permitted = False


@login_required
def licensing(request, slug=None):
    user = request.user
    if slug:
        wells = Well.objects.all()
        current_well = Well.objects.get(slug=slug)

        inst1 = ChargeAndCredit.objects.get(well=current_well)
        inst2 = TechnicalCondition.objects.get(well=current_well)
        inst3 =  ModifyName.objects.get(well=current_well)
        inst4 = Commitment.objects.get(well=current_well)
        inst5 = Issuance.objects.get(well=current_well)

        form1 = ChargeAndCreditForm(instance = inst1)
        form2 = TechnicalConditionForm(instance = inst2)
        form3 = ModifyNameForm(instance = inst3)
        form4 = CommitmentForm(instance = inst4)
        form5 = IssuanceForm(instance = inst5)
        # form6 = BeneficiaryForm()

        BeneficiaryFormSet = formset_factory(BeneficiaryForm, extra=0,)
        # BeneficiaryFormSet = formset_factory(BeneficiaryForm, extra=0, formset=RequiredFormSet)

        if 'form1' in request.POST:
            form1 = ChargeAndCreditForm(request.POST, request.FILES, instance=inst1)
            if form1.is_valid():
                obj = form1.save(commit=False)
                obj.creator = user
                obj.save()
                messages.success(request,'اطلاعات وضعیت شارژ و اعتبار با موفقیت ثبت شد')
                return redirect('dashboard:licensing', slug=slug )

        if 'form2' in request.POST:
            form2 = TechnicalConditionForm(request.POST, request.FILES, instance=inst2)
            if form2.is_valid():
                obj = form2.save(commit=False)
                obj.creator = user
                obj.save()
                messages.success(request,'اطلاعات وضعیت فنی با موفقیت ثبت شد')
                return redirect('dashboard:licensing', slug=slug )
                # return redirect('dashboard:profile')

        if 'form3' in request.POST:
            form3 = ModifyNameForm(request.POST, request.FILES, instance=inst3)
            if form3.is_valid():
                obj = form3.save(commit=False)
                obj.creator = user
                obj.save()
                messages.success(request,'اطلاعات اصلاح نام با موفقیت ثبت شد')
                return redirect('dashboard:licensing', slug=slug )
                # return redirect('dashboard:profile')

        if 'form4' in request.POST:
            form4 = CommitmentForm(request.POST, request.FILES, instance=inst4)
            if form4.is_valid():
                obj = form4.save(commit=False)
                obj.creator = user
                obj.save()
                messages.success(request,'اطلاعات تعهد نمایندگی فروش با موفقیت ثبت شد')
                return redirect('dashboard:licensing', slug=slug )
                # return redirect('dashboard:profile')

        if 'form5' in request.POST:
            form5 = IssuanceForm(request.POST, request.FILES, instance=inst5)
            if form5.is_valid():
                obj = form5.save(commit=False)
                obj.creator = user
                obj.save()
                messages.success(request,'اطلاعات بررسی نهایی و صدور فرم با موفقیت ثبت شد')
                return redirect('dashboard:licensing', slug=slug )
                # return redirect('dashboard:profile')

        if 'form6' in request.POST:
            formset = BeneficiaryFormSet(request.POST)
            if formset.is_valid():
                for form in formset:
                    if form.cleaned_data:
                        child = form.save(commit=False)
                        child.creator = user
                        child.well = current_well
                        child.save()
                        messages.success(request,'بهره‌بردار جدید باموفقیت اضافه شد')
                return redirect('dashboard:licensing', slug=slug )
                # return redirect('dashboard:profile')
        # if 'form6' in request.POST:
        #     form6 = BeneficiaryForm(request.POST, request.FILES)
        #     if form6.is_valid():
        #         obj = form6.save(commit=False)
        #         obj.creator = user
        #         obj.well = current_well
        #         obj.save()
        #         messages.success(request,'بهره‌بردار جدید باموفقیت اضافه شد')
        #         return redirect('dashboard:licensing', slug=slug )
        #         # return redirect('dashboard:profile')


        context={
            'wells':wells,
            'form1': form1,
            'form2': form2,
            'form3': form3,
            'form4': form4,
            'form5': form5,
            # 'form6': form6,
            'formset': BeneficiaryFormSet,
            'current_well':current_well,
            'slug':slug,
            }
    else:
        wells = Well.objects.all()
        context={
            'wells':wells,
            }
    return render(request,"dashboard/licensing.html", context)
