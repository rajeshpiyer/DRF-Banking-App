#LOCATION FROM PINCODE
# import pgeocode

# def get_city_from_pincode(pincode):
#     nomi = pgeocode.Nominatim('in')
#     location_info = nomi.query_postal_code(pincode)
#     state = location_info['state_name']
#     district = location_info['county_name']
#     city = location_info['place_name']
#     return state, district, city

# pincode = '686141'
# state,district,city = get_city_from_pincode(pincode)
# print("City corresponding to PIN code", pincode, "is", city," District : ",district," State : ",state)

from rest_framework import generics,filters,status
from .models import *
from .serializers import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum
from django.core.mail import send_mail
import datetime

#-------------------------------#
#--------ALL USERS--------------#
#-------------------------------#

class UserRegistrationAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class UserLoginView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = response.data['access']
        print(token)
        response.set_cookie('jwt', token, max_age=3600, httponly=True)
        return response


#-------------------------------#
#--------STAFF ONLY-------------#
#-------------------------------#

#ACCOUNT TYPE
class AccountTypeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return AccountType.objects.get(pk=pk)
        except AccountType.DoesNotExist:
            return None

    def get(self, request, pk=None, *args, **kwargs):
        if pk is not None:
            account_type = self.get_object(pk)
            if account_type is None:
                return Response({"error": "Account type not found."}, status=status.HTTP_404_NOT_FOUND)
            serializer = AccountTypeSerializer(account_type)
            return Response(serializer.data)
        else:
            account_types = AccountType.objects.all()
            serializer = AccountTypeSerializer(account_types, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        if request.user.user_type != 'staff':
            return Response({"error": "Only staff members can perform this action."}, status=status.HTTP_403_FORBIDDEN)

        serializer = AccountTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        if request.user.user_type != 'staff':
            return Response({"error": "Only staff members can perform this action."}, status=status.HTTP_403_FORBIDDEN)

        account_type = self.get_object(pk)
        if account_type is None:
            return Response({"error": "Account type not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = AccountTypeSerializer(account_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        if request.user.user_type != 'staff':
            return Response({"error": "Only staff members can perform this action."}, status=status.HTTP_403_FORBIDDEN)

        account_type = self.get_object(pk)
        if account_type is None:
            return Response({"error": "Account type not found."}, status=status.HTTP_404_NOT_FOUND)

        account_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#LOAN TYPE
class LoanTypeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return LoanType.objects.get(pk=pk)
        except LoanType.DoesNotExist:
            return None

    def get(self, request, pk=None, *args, **kwargs):
        if pk is not None:
            loan_type = self.get_object(pk)
            if loan_type is None:
                return Response({"error": "Loan type not found."}, status=status.HTTP_404_NOT_FOUND)
            serializer = LoanTypeSerializer(loan_type)
            return Response(serializer.data)
        else:
            loan_types = LoanType.objects.all()
            serializer = LoanTypeSerializer(loan_types, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        if request.user.user_type != 'staff':
            return Response({"error": "Only staff members can perform this action."}, status=status.HTTP_403_FORBIDDEN)

        serializer = LoanTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        if request.user.user_type != 'staff':
            return Response({"error": "Only staff members can perform this action."}, status=status.HTTP_403_FORBIDDEN)

        loan_type = self.get_object(pk)
        if loan_type is None:
            return Response({"error": "Loan type not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = LoanTypeSerializer(loan_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        if request.user.user_type != 'staff':
            return Response({"error": "Only staff members can perform this action."}, status=status.HTTP_403_FORBIDDEN)

        loan_type = self.get_object(pk)
        if loan_type is None:
            return Response({"error": "Loan type not found."}, status=status.HTTP_404_NOT_FOUND)

        loan_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#---------------------------------------------#
#------------CUSTOMER ONLY-------------------#
#---------------------------------------------#

#Accounts

class AccountAPIView(APIView):
    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'staff':
            return Account.objects.all()
        elif user.user_type == 'customer':
            return Account.objects.filter(user=user)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        data = []
        for account in queryset:
            account_data = str(account.get_account_number())+" : "+f"{account.user.first_name} {account.user.last_name}"+" : "+account.account_type.name+" : "+str(account.balance)
            data.append(account_data)
        return Response(data)

    def post(self, request, *args, **kwargs):
        if request.user.user_type != 'customer':
            return Response({"error": "Only customers can create accounts."}, status=status.HTTP_403_FORBIDDEN)

        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)

            #--------Email Alert-----------------------------------------------
            sender = "prajeshiyer@gmail.com"
            recipient = [request.user.email]
            subject_to_applicant = "Account Created"
            message_to_applicant = "Congratulations! New Account Created Successfully!!"
            send_mail(subject_to_applicant, message_to_applicant, sender, recipient)
            #--------Email Alert-----------------------------------------------

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#------------DEPOSIT

class DepositAPIView(APIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        if user.user_type != 'customer':
            return Response({"error": "Only customers can deposit amounts."}, status=status.HTTP_403_FORBIDDEN)

        try:
            account_number = request.data.get('account_number')
            accounts = Account.objects.all()
            for i in accounts:
                if i.get_account_number() == account_number:
                    account = i
                    break
            #account = Account.objects.get(user=user, id=request.data.get('account_id'))
        except Account.DoesNotExist:
            return Response({"error": "Account not found."}, status=status.HTTP_404_NOT_FOUND)

        amount = int(request.data.get('amount'))
        purpose = request.data.get('purpose')
        if not amount:
            return Response({"error": "Amount to deposit must be provided."}, status=status.HTTP_400_BAD_REQUEST)
        if not purpose:
            return Response({"error": "Purpose to deposit must be provided."}, status=status.HTTP_400_BAD_REQUEST)
        
        account.balance += amount
        account.save()

        transaction_data = {
            'account': account.id,
            'particulars': 'Deposit',
            'credit': amount,
            'balance': account.balance,
            'purpose': purpose
        }
        serializer = TransactionSerializer(data=transaction_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#-------------WITHDRAW

class WithdrawAPIView(APIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        if user.user_type != 'customer':
            return Response({"error": "Only customers can withdraw amounts."}, status=status.HTTP_403_FORBIDDEN)

        try:
            account_number = request.data.get('account_number')
            accounts = Account.objects.all()
            for i in accounts:
                if i.get_account_number() == account_number:
                    account = i
                    break
            #account = Account.objects.get(user=user, id=request.data.get('account_id'))
        except Account.DoesNotExist:
            return Response({"error": "Account not found."}, status=status.HTTP_404_NOT_FOUND)

        amount = int(request.data.get('amount'))
        purpose = request.data.get('purpose')
        if not amount:
            return Response({"error": "Amount to withdraw must be provided."}, status=status.HTTP_400_BAD_REQUEST)
        
        if not purpose:
            return Response({"error": "Purpose to withdraw must be provided."}, status=status.HTTP_400_BAD_REQUEST)
        
        if account.balance < amount:
            return Response({"error": "Insufficient balance."}, status=status.HTTP_400_BAD_REQUEST)

        account.balance -= amount

        #Budget Tracking
        #-------------------------------------------------------------#
        today = datetime.date.today()
        first_day_of_month = today.replace(day=1)
        last_day_of_month = today.replace(day=1, month=today.month % 12 + 1) - datetime.timedelta(days=1)

        total_expenditure = Transaction.objects.filter(
        account=account,
        timestamp__gte=first_day_of_month,
        timestamp__lte=last_day_of_month,
        debit__isnull=False
        ).aggregate(total=Sum('debit'))

        total_expenditure_amount = total_expenditure['total'] or 0
        
        #Fetching Budget
        budget = MonthlyBudget.objects.get(account=account)
        if budget:
            if total_expenditure_amount > budget.budget:
                #--------Email Alert-----------------------------------------------
                sender = "prajeshiyer@gmail.com"
                recipient = [request.user.email]
                subject_to_applicant = "Budget Exceeded"
                message_to_applicant = "Watch your expenses, This month's budget exceeded for Account Number : "+account.get_account_number()
                send_mail(subject_to_applicant, message_to_applicant, sender, recipient)
                #--------Email Alert-----------------------------------------------
        #-----------------------------------------------------------------------------------------#


        account.save()

        transaction_data = {
            'account': account.id,
            'particulars': 'Withdrawal',
            'debit': amount,
            'balance': account.balance,
            'purpose': purpose
        }
        serializer = TransactionSerializer(data=transaction_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#----------------ACCOUNT TRANSFER

class TransferAPIView(APIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        if user.user_type != 'customer':
            return Response({"error": "Only customers can perform transfers."}, status=status.HTTP_403_FORBIDDEN)

        from_account_number = request.data.get('from_account_number')
        to_account_number = request.data.get('to_account_number')
        amount = request.data.get('amount')
        purpose = request.data.get('purpose')

        if not all([from_account_number, to_account_number, amount, purpose]):
            return Response({"error": "From account, to account,purpose and amount must be provided."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            from_account = None
            accounts = Account.objects.filter(user=user)
            for i in accounts:
                if i.get_account_number() == from_account_number:
                    from_account = i
                    break
            if not from_account:
                raise Account.DoesNotExist
            
            to_account = None
            accounts = Account.objects.filter(user=user)
            for i in accounts:
                if i.get_account_number() == to_account_number:
                    to_account = i
                    break
            if not to_account:
                raise Account.DoesNotExist
        except Account.DoesNotExist:
            return Response({"error": "One or both accounts not found."}, status=status.HTTP_404_NOT_FOUND)

        if from_account.balance < int(amount):
            return Response({"error": "Insufficient balance in from account."}, status=status.HTTP_400_BAD_REQUEST)

        from_account.balance -= int(amount)
        to_account.balance += int(amount)
        from_account.save()
        to_account.save()

        particulars = f"TRF to {to_account.__str__()}"
        Transaction.objects.create(account=from_account, particulars=particulars, debit=amount, balance=from_account.balance, purpose=purpose)
        Transaction.objects.create(account=to_account, particulars=f"TRF from {from_account}", credit=amount, balance=to_account.balance, purpose=purpose)

        #Budget Tracking
        #-------------------------------------------------------------#
        today = datetime.date.today()
        first_day_of_month = today.replace(day=1)
        last_day_of_month = today.replace(day=1, month=today.month % 12 + 1) - datetime.timedelta(days=1)

        total_expenditure = Transaction.objects.filter(
        account=from_account,
        timestamp__gte=first_day_of_month,
        timestamp__lte=last_day_of_month,
        debit__isnull=False
        ).aggregate(total=Sum('debit'))

        total_expenditure_amount = total_expenditure['total'] or 0
        
        #Fetching Budget
        budget = MonthlyBudget.objects.get(account=from_account)
        if budget:
            if total_expenditure_amount > budget.budget:
                #--------Email Alert-----------------------------------------------
                sender = "prajeshiyer@gmail.com"
                recipient = [request.user.email]
                subject_to_applicant = "Budget Exceeded"
                message_to_applicant = "Watch your expenses, This month's budget exceeded for Account Number : "+from_account.get_account_number()
                send_mail(subject_to_applicant, message_to_applicant, sender, recipient)
                #--------Email Alert-----------------------------------------------
        #-----------------------------------------------------------------------------------------#


        return Response({"message": "Transfer successful."}, status=status.HTTP_200_OK)

#-----Account Statement
class AccountStatementAPIView(APIView):

    def get(self, request, account_number, *args, **kwargs):
        user = request.user
        if user.user_type != 'customer':
            return Response({"error": "Only customers can View Statements."}, status=status.HTTP_403_FORBIDDEN)

        try:
            account = None
            accounts = Account.objects.filter(user=user)
            for i in accounts:
                if i.get_account_number() == account_number:
                    account = i
                    break
            if not account:
                raise Account.DoesNotExist
        except Account.DoesNotExist:
            return Response({"error": "Account not found or does not belong to the user."}, status=status.HTTP_404_NOT_FOUND)

        data=[]
        data.append("Date&Time : Particulars : Debit : Credit : Balance")
        data.append(" ")
        transactions = Transaction.objects.filter(account=account).order_by('timestamp')
        #serializer = TransactionSerializer(transactions, many=True)
        for i in transactions:
            data.append(str(i.timestamp)+" : "+i.particulars+" : "+str(i.debit)+" : "+str(i.credit)+" : "+str(i.balance))
        return Response(data)

#---------LOANS----------#

#--------APPLY FOR LOAN-----

class LoanApplicationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        if user.user_type != 'customer':
            return Response({"error": "Only customers can apply for loans."}, status=status.HTTP_403_FORBIDDEN)
        
        accounts = Account.objects.filter(user=user, account_type__id=1)
        if not accounts:
            return Response({"error": "Only customers with Savings account can apply for loans."}, status=status.HTTP_403_FORBIDDEN)

        
        serializer = LoanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user, status='Applied')
            #--------Email Alert-----------------------------------------------
            sender = "prajeshiyer@gmail.com"
            recipient = [request.user.email]
            subject_to_applicant = "Applied For Loan"
            message_to_applicant = "Successfully Submitted Application for Loan"
            send_mail(subject_to_applicant, message_to_applicant, sender, recipient)
            #--------Email Alert-----------------------------------------------
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#----LOAN STATUS UPDATE--------
class LoanStatusUpdateAPIView(APIView):

    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'staff':
            return Loan.objects.filter(status="Applied")
        elif user.user_type == 'customer':
            return Loan.objects.filter(user=user)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        data = []
        if not queryset:
            data.append("No Loans to Show!")
        else:
            for loan in queryset:
                loan_data = str(loan.id)+" : "+f"{loan.user.first_name} {loan.user.last_name}"+" : "+loan.loan_type.name+" : "+str(loan.amount)+" : "+loan.status
                data.append(loan_data)
        return Response(data)


    def patch(self, request, pk, *args, **kwargs):
        try:
            loan = Loan.objects.get(pk=pk)
        except Loan.DoesNotExist:
            return Response({"error": "Loan not found."}, status=status.HTTP_404_NOT_FOUND)

        if request.user.user_type != 'staff':
            return Response({"error": "Only staff members can update loan status."}, status=status.HTTP_403_FORBIDDEN)
        
        if loan.status!="Applied":
            return Response({"error": "Loan already Resolved."}, status=status.HTTP_403_FORBIDDEN)

        status1 = request.data.get('status')
        if not status1:
            return Response({"error": "Status must be provided for update."}, status=status.HTTP_400_BAD_REQUEST)

        loan.status = status1
        loan.save()

        #--------Email Alert-----------------------------------------------
        sender = "prajeshiyer@gmail.com"
        recipient = [request.user.email]
        subject_to_applicant = "Loan Approved"
        message_to_applicant = "Congratulations!! Your "+loan.loan_type.name+" for "+loan.amount+" is Approved!"
        send_mail(subject_to_applicant, message_to_applicant, sender, recipient)
        #--------Email Alert-----------------------------------------------

        accounts = Account.objects.filter(user=loan.user, account_type__id=1)
        for i in accounts:
            account = i
        account.balance += loan.amount
        account.save()
        Transaction.objects.create(account=account, particulars="TRF From "+loan.loan_type.name, credit=loan.amount, balance=account.balance, purpose="Loan")
        return Response({"message": "Loan Approved successfully."}, status=status.HTTP_200_OK)

#------LOAN REPAYMENT---------

class LoanRepaymentAPIView(APIView):

    def get_active_loans(self, user):
        return Loan.objects.filter(user=user, status='Active')

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.user_type != 'customer':
            return Response({"error": "Only customers can Repay Loans."}, status=status.HTTP_403_FORBIDDEN)
        
        active_loans = self.get_active_loans(user)
        serializer = LoanSerializer(active_loans, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        user = request.user
        if user.user_type != 'customer':
            return Response({"error": "Only customers can Repay Loans."}, status=status.HTTP_403_FORBIDDEN)
        
        data = request.data

        try:
            from_account_number = data.get('from_account')
            account = None
            accounts = Account.objects.filter(user=user)
            for i in accounts:
                if i.get_account_number() == from_account_number:
                    account = i
                    break
            if not account:
                raise Account.DoesNotExist
        except Account.DoesNotExist:
            return Response({"error": "From account not found or does not belong to the user."}, status=status.HTTP_404_NOT_FOUND)

        try:
            to_loan_id = data.get('to_loan')
            to_loan = Loan.objects.get(id=to_loan_id, user=user)
        except Loan.DoesNotExist:
            return Response({"error": "Loan not found or does not belong to the user."}, status=status.HTTP_404_NOT_FOUND)
        
        if to_loan.status!= 'Active':
            return Response({"error": "Loan is yet to Approve"}, status=status.HTTP_403_FORBIDDEN)
        
        amount = int(data.get('amount'))

        if amount <= 0:
            return Response({"error": "Repayment amount should be greater than zero."}, status=status.HTTP_400_BAD_REQUEST)
        elif amount > account.balance:
            return Response({"error": "Insufficient Balance in your Account."}, status=status.HTTP_400_BAD_REQUEST)
        data ={
                "from_account" : account.id,
                "to_loan" : request.data.get('to_loan'),
                "amount" : request.data.get('amount'),
            }
        serializer = RepaymentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            #--------Email Alert-----------------------------------------------
            sender = "prajeshiyer@gmail.com"
            recipient = [request.user.email]
            subject_to_applicant = "Repayment Recieved"
            message_to_applicant = "Repayment of"+ str(amount) +" recieved for "+to_loan.loan_type.name+" : "+str(to_loan.id)
            send_mail(subject_to_applicant, message_to_applicant, sender, recipient)
            #--------Email Alert-----------------------------------------------

            # Update loan status
            to_loan.amount -= amount
            if to_loan.amount <= 0:
                to_loan.status = 'Closed'
                #--------Email Alert-----------------------------------------------
                sender = "prajeshiyer@gmail.com"
                recipient = [request.user.email]
                subject_to_applicant = "Repayment Recieved"
                message_to_applicant = "Your "+to_loan.loan_type.name+" : "+to_loan.id+" is Closed as Full repayment recieved."
                send_mail(subject_to_applicant, message_to_applicant, sender, recipient)
                #--------Email Alert-----------------------------------------------
            to_loan.save()

            account.balance -= amount
            account.save()

            Transaction.objects.create(account=account, particulars="TRF to "+to_loan.loan_type.name+" - "+str(to_loan.id), debit=amount, balance=account.balance, purpose="Loan Repayment")

            #Budget Tracking
            #-------------------------------------------------------------#
            today = datetime.date.today()
            first_day_of_month = today.replace(day=1)
            last_day_of_month = today.replace(day=1, month=today.month % 12 + 1) - datetime.timedelta(days=1)

            total_expenditure = Transaction.objects.filter(
            account=account,
            timestamp__gte=first_day_of_month,
            timestamp__lte=last_day_of_month,
            debit__isnull=False
            ).aggregate(total=Sum('debit'))

            total_expenditure_amount = total_expenditure['total'] or 0
        
            #Fetching Budget
            budget = MonthlyBudget.objects.get(account=account)
            if budget:
                if total_expenditure_amount > budget.budget:
                    #--------Email Alert-----------------------------------------------
                    sender = "prajeshiyer@gmail.com"
                    recipient = [request.user.email]
                    subject_to_applicant = "Budget Exceeded"
                    message_to_applicant = "Watch your expenses, This month's budget exceeded for Account Number : "+account.get_account_number()
                    send_mail(subject_to_applicant, message_to_applicant, sender, recipient)
                    #--------Email Alert-----------------------------------------------
            #-----------------------------------------------------------------------------------------#

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#-------MONTHLY BUDGET---------

class MonthlyBudgetAPIView(APIView):

    def post(self, request, *args, **kwargs):
        user = request.user
        if user.user_type != 'customer':
            return Response({"error": "Only customers can set Budgets."}, status=status.HTTP_403_FORBIDDEN)
        account_number = request.data.get('account_number')
        budget = request.data.get('budget')

        if not all([account_number, budget]):
            return Response({"error": "Account number and budget must be provided."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            account = None
            accounts = Account.objects.filter(user=user)
            for i in accounts:
                if i.get_account_number() == account_number:
                    account = i
                    break
            if not account:
                raise Account.DoesNotExist
        except Account.DoesNotExist:
            return Response({"error": "Account not found."}, status=status.HTTP_404_NOT_FOUND)

        try:
            monthly_budget = MonthlyBudget.objects.get(account=account)
            monthly_budget.budget = budget
            monthly_budget.save()
            serializer = MonthlyBudgetSerializer(monthly_budget)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except MonthlyBudget.DoesNotExist:
            monthly_budget = MonthlyBudget.objects.create(account=account, budget=budget)
            serializer = MonthlyBudgetSerializer(monthly_budget)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

#---------EXPENSE TRACKING-------
class ExpenseTrackingAPIView(APIView):

    def get(self, request, account_number, *args, **kwargs):
        user = request.user
        if user.user_type != 'customer':
            return Response({"error": "Only customers can Track Expenses."}, status=status.HTTP_403_FORBIDDEN)

        try:
            account = None
            accounts = Account.objects.filter(user=user)
            for i in accounts:
                if i.get_account_number() == account_number:
                    account = i
                    break
            if not account:
                raise Account.DoesNotExist
        except Account.DoesNotExist:
            return Response({"error": "Account not found or does not belong to the user."}, status=status.HTTP_404_NOT_FOUND)

        total_expenditure = Transaction.objects.filter(account=account, debit__isnull=False).aggregate(total=Sum('debit'))['total']
        if total_expenditure is None:
            total_expenditure = 0

        expenditures_by_purpose = Transaction.objects.filter(account=account, debit__isnull=False).values('purpose').annotate(total=Sum('debit'))

        data = {
            "total_expenditure": total_expenditure,
            "expenditures_by_purpose": expenditures_by_purpose
        }
        return Response(data)

