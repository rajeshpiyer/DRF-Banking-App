#-------Packages-------------------
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator
#-----------------------------------

#------------USER------------

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('customer', 'Customer'),
        ('staff', 'Staff'),
    )
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Pending', 'Pending'),
    )

    address = models.CharField(max_length=255)
    pincode = models.CharField(max_length=10)
    mobile = models.CharField(max_length=10)
    aadhar_number = models.CharField(max_length=12, validators=[MinLengthValidator(12)])
    pan_number = models.CharField(max_length=10, validators=[MinLengthValidator(10)])
    photo = models.ImageField(upload_to='user_photos/', null=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,default='Pending')

    def __str__(self):
        return self.first_name+self.last_name

#--------BANK---------

#ACCOUNTS
#-------Types

class AccountType(models.Model):
    name = models.CharField(max_length=100)
    min_balance = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

#-------Accounts

class Account(models.Model):
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Closed', 'Closed'),
    )

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    account_type = models.ForeignKey(AccountType, on_delete=models.CASCADE)
    opening_date = models.DateTimeField(default=timezone.now)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.user.first_name} - {self.account_type.name} - {self.get_account_number()}"
    
    def get_account_number(self):
        return f"{str(self.user.id)}{str(self.account_type.id)}{str(self.id)}"
    



#TRANSACTIONS

class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    particulars = models.CharField(max_length=255)
    debit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    credit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    purpose = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.timestamp} - {self.particulars}"
    
#LOANS

#------------Loan Types
class LoanType(models.Model):
    name = models.CharField(max_length=100)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    eligibility = models.CharField(max_length=255)

    def __str__(self):
        return self.name

#-----------Loans
class Loan(models.Model):
    STATUS_CHOICES = (
        ('Applied', 'Applied'),
        ('Active', 'Active'),
        ('Closed', 'Closed'),
    )

    timestamp = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    loan_type = models.ForeignKey(LoanType, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    tenure = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.user.first_name} - {self.loan_type.name} - {str(self.id)}"

#----------Repayment
class Repayment(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    from_account = models.ForeignKey(Account, on_delete=models.CASCADE)
    to_loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Repayment: {self.from_account.user.username} - {self.amount}"

#----BUDGETING TOOLS----------

#--------Monthly Budget
class MonthlyBudget(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    budget = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.account.user.username} - Budget: {self.budget}"


