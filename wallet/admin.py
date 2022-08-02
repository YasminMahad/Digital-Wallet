from django.contrib import admin
from .models import  Account, Card, Customer, Loan, Notification, Receipt, Reward, Thirdparty, Transaction, Wallet

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("firstname","lastname","address","email","phone_number","age","gender","nationality","martialStatus","employment_status","signature")
    search_fields = ("firstname","lastname","address","email","phone_number","age","gender","nationality","martialStatus","employment_status","signature")

admin.site.register(Customer,CustomerAdmin)
admin.site.register(Wallet)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Card)
admin.site.register(Thirdparty)
admin.site.register(Notification)
admin.site.register(Receipt)
admin.site.register(Loan)
admin.site.register(Reward)
