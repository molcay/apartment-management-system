from django.contrib.auth.models import User
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework.validators import UniqueValidator

from api.models import Guarantor, Tenant, Landlord, Room, Agreement


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
        if not validate_tc(value):
            raise serializers.ValidationError('Username must be T.C. ID.')
        return value


def validate_tc(value):
    if not (len(value) == 11 and value.isdigit() and value[0] != '0' and value[-1] in '02468'):
        return False
    digits = [int(c) for c in value]
    tenth_digit = ((sum(digits[:9:2]) * 7) - (sum(digits[1:9:2]))) % 10
    is_tenth_digit_valid = tenth_digit == digits[9]
    if not is_tenth_digit_valid:
        return False
    eleventh_digit = sum(digits[:-1]) % 10
    is_eleventh_digit_valid = eleventh_digit == digits[-1]
    if not is_eleventh_digit_valid:
        return False
    return True
