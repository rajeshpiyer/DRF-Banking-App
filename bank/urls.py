from django.urls import path
from .views import *

urlpatterns = [
    #ALL USERS
    path('register/', UserRegistrationAPIView.as_view(), name='user_register'),
    path('', UserLoginView.as_view(), name='user_login'),

   
    path('account_types/', AccountTypeAPIView.as_view(), name='account_types_list'),
    path('account_types/<int:pk>/', AccountTypeAPIView.as_view(), name='account_type_detail'),
    path('loan_types/', LoanTypeAPIView.as_view(), name='loan_types_list'),
    path('loan_types/<int:pk>/', LoanTypeAPIView.as_view(), name='loan_type_detail'),
    path('accounts/', AccountAPIView.as_view(), name='account-create-update'),

    path('deposit/', DepositAPIView.as_view(), name='deposit'),
    path('withdraw/', WithdrawAPIView.as_view(), name='withdraw'),
    path('transfer/', TransferAPIView.as_view(), name='transfer'),
    path('account-statement/<str:account_number>/', AccountStatementAPIView.as_view(), name='account-statement'),

    path('apply_loan/', LoanApplicationAPIView.as_view(), name='transfer'),
    path('loan_status/<int:pk>/', LoanStatusUpdateAPIView.as_view(), name='transfer'),
    path('loan-repayment/', LoanRepaymentAPIView.as_view(), name='loan-repayment'),

    path('monthly-budget/', MonthlyBudgetAPIView.as_view(), name='monthly-budget'),
    path('expense-tracking/<str:account_number>/', ExpenseTrackingAPIView.as_view(), name='expense-tracking'),
]
