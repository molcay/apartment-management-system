from django.contrib.auth.models import User
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework.validators import UniqueValidator

from api.models import Guarantor, Tenant, Landlord, Room, Agreement
from project.utils.TurkishIdentityNumberUtils import TurkishIdentityNumberUtils


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
