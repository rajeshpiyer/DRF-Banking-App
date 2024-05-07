from django.contrib import admin
from .models import CustomUser, AccountType, Account, Transaction, LoanType, Loan, Repayment, MonthlyBudget

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'first_name', 'last_name', 'address', 'pincode', 'mobile', 'aadhar_number', 'pan_number', 'photo', 'user_type', 'status']

class AccountTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'min_balance', 'interest_rate']

class AccountAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'account_type', 'opening_date', 'balance', 'status']

class TransactionAdmin(admin.ModelAdmin):
    list_display = ['id', 'account', 'timestamp', 'particulars', 'debit', 'credit', 'balance', 'purpose']

class LoanTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'interest_rate', 'eligibility']

class LoanAdmin(admin.ModelAdmin):
    list_display = ['id', 'timestamp', 'user', 'loan_type', 'amount', 'tenure', 'status']

class RepaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'timestamp', 'from_account', 'to_loan', 'amount']

class MonthlyBudgetAdmin(admin.ModelAdmin):
    list_display = ['id', 'account', 'budget']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(AccountType, AccountTypeAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(LoanType, LoanTypeAdmin)
admin.site.register(Loan, LoanAdmin)
admin.site.register(Repayment, RepaymentAdmin)
admin.site.register(MonthlyBudget, MonthlyBudgetAdmin)
