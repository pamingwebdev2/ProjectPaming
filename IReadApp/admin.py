from django.contrib import admin
from .models import Borrower, Item, BorrTrans, DonTrans, Penalty


admin.site.register(Borrower)
admin.site.register(Item)
admin.site.register(BorrTrans)
admin.site.register(DonTrans)
admin.site.register(Penalty)
# Register your models here.
