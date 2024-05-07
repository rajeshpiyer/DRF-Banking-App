from rest_framework import serializers
from .models import CustomUser, AccountType, Account, Transaction, LoanType, Loan, Repayment, MonthlyBudget
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name','username', 'password', 'email', 'address', 'pincode','mobile','aadhar_number','pan_number','photo','user_type')

    def validate(self, data):
        # Check if a user with the given Aadhar number already exists
        if CustomUser.objects.filter(aadhar_number=data.get('aadhar_number')).exists():
            raise serializers.ValidationError("A user with this Aadhar number already exists.")

        # Check if a user with the given PAN number already exists
        if CustomUser.objects.filter(pan_number=data.get('pan_number')).exists():
            raise serializers.ValidationError("A user with this PAN number already exists.")

        return data
    
    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user



class AccountTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountType
        fields = '__all__'

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('account_type','balance')

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class LoanTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanType
        fields = '__all__'

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ('loan_type','amount','tenure')

class RepaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repayment
        fields = ('from_account','to_loan','amount')

class MonthlyBudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlyBudget
        fields = '__all__'
