from django.shortcuts import render
from receipts.models import ExpenseCategory, Account, Receipt
from django.contrib.auth.decorators import login_required

# Create your views here.


## def receipt_list(request):
##    receipts = Receipt.objects.all()
##    context = {
##        "receipts": receipts,
##    }
##    return render(request, "receipts/list.html", context)


@login_required
def receipt_list(request):
    receipts = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipts": receipts,
    }
    return render(request, "receipts/list.html", context)
