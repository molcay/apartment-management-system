from rest_framework import serializers

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
    