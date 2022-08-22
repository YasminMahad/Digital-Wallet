from django.contrib import admin
from .models import  Account, Card, Customer, Loan, Notification, Receipt, Reward, Thirdparty, Transaction, Wallet

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("firstname","lastname","address","email","phone_number","age","gender","nationality","martialStatus","employment_status","signature",)
    search_fields = ("firstname","lastname","address","email","phone_number","age","gender","nationality","martialStatus","employment_status","signature",)

admin.site.register(Customer)

class WalletAdmin(admin.ModelAdmin):
    list_display = ["balance","customer","pin","isActive","dateCreated","currency",]
    search_fields = ["balance","customer","pin","isActive","dateCreated","currency",]

admin.site.register(Wallet,WalletAdmin)

class CardAdmin(admin.ModelAdmin):
    list_display= ["issue_date","card_name","card_number","card_type","expiry_date","card_status","security_code","wallet","account","issuer",]
    search_fields = ["issue_date","card_name","card_number","card_type","expiry_date","card_status","security_code","wallet","account","issuer",]

admin.site.register(Card,CardAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display = ("account_number","account_type","balance","wallet")
    search_fields = ("account_number","account_type","balance","wallet")

admin.site.register(Account,AccountAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ("transaction_code","wallet","transaction_amount","transaction_type","transaction_charge","transaction_date","transactionreciept","origin_account")
    search_fields = ("transaction_code","wallet","transaction_amount","transaction_type","transaction_charge","transaction_date","transaction_reciept","origin_account")

admin.site.register(Transaction,TransactionAdmin)

class ThirdpartyAdmin(admin.ModelAdmin):
    list_display = ("name","transaction_amount","account","currency","location","phone_number")
    search_fields = ("name","transaction_amount","account","currency","location","phone_number")

admin.site.register(Thirdparty,ThirdpartyAdmin)

class NotificationAdmin(admin.ModelAdmin):
    list_display= ("name","recipient","status","date_and_time")
    search_fields= ("name","recipient","status","date_and_time")

admin.site.register(Notification,NotificationAdmin)

class ReceiptAdmin(admin.ModelAdmin):
    list_display= ("receipt_type","receipt_date","bill_number","total_amount","receipt_file")
    search_fields= ("receipt_type","receipt_date","bill_number","total_amount","receipt_file")

admin.site.register(Receipt,ReceiptAdmin)

class LoanAdmin(admin.ModelAdmin):
    list_display= ("loan_id","loan_type","amount","wallet","interest_rate","payment_due_date","loan_balance","loan_Term","guarantor")
    search_fields= ("loan_id","loan_type","amount","wallet","interest_rate","payment_due_date","loan_balance","loan_Term","guarantor")

admin.site.register(Loan,LoanAdmin)

class RewardAdmin(admin.ModelAdmin):
    list_display= ("name","bonus","gender","reward_points","date_of_reward","recipient")
    search_fields= ("name","bonus","gender","reward_points","date_of_reward","recipient")


admin.site.register(Reward,RewardAdmin)
