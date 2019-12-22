from django.contrib.auth.models import User
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework.validators import UniqueValidator

from api.models import Guarantor, Tenant, Landlord, Room, Agreement, Issue
from project.utils.TurkishIdentityNumberUtils import TurkishIdentityNumberUtils


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'date_joined', 'last_login')


class IssueUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'


class IssueSerializer(IssueUpdateSerializer):
    created_by = UserDetailSerializer()


class GuarantorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guarantor
        fields = '__all__'


class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = '__all__'


class LandlordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Landlord
        fields = '__all__'


class RoomUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class RoomSerializer(RoomUpdateSerializer):
    landlord = LandlordSerializer()


class AgreementUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agreement
        fields = '__all__'


class AgreementSerializer(AgreementUpdateSerializer):
    room = RoomSerializer()
    tenant = TenantSerializer()
    guarantor = GuarantorSerializer()


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )

    def validate_username(self, value: str):
        if not TurkishIdentityNumberUtils.validate(value):
            raise serializers.ValidationError('Username must be T.C. ID.')
        return value
