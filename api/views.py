from django.http import JsonResponse
from rest_framework import generics, viewsets, filters

from api.doc_manager.manager import DocManager
from api.models import Tenant, Guarantor, Landlord, Room, Agreement, AgreementFile
from api.serializers import TenantSerializer, GuarantorSerializer, LandlordSerializer, RoomSerializer, \
    AgreementSerializer, RoomUpdateSerializer, AgreementUpdateSerializer


class TenantListCreateView(generics.ListCreateAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name']


class TenantRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer



class GuarantorListCreateView(generics.ListCreateAPIView):
    queryset = Guarantor.objects.all()
    serializer_class = GuarantorSerializer


class GuarantorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guarantor.objects.all()
    serializer_class = GuarantorSerializer


class LandlordListCreateView(generics.ListCreateAPIView):
    queryset = Landlord.objects.all()
    serializer_class = LandlordSerializer


class LandlordRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Landlord.objects.all()
    serializer_class = LandlordSerializer


class RoomListCreateView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    # serializer_class = RoomSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return RoomUpdateSerializer
        return RoomSerializer

class GuarantorListCreateView(generics.ListCreateAPIView):
    queryset = Guarantor.objects.all()
    # serializer_class = RoomSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return GuarantorSerializer
        return GuarantorSerializer

class RoomRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    # serializer_class = RoomSerializer

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return RoomUpdateSerializer
        return RoomSerializer


class BaseViewSet(viewsets.ModelViewSet):    # TODO: add permissions here
    pass


class AgreementViewSet(BaseViewSet):
    queryset = Agreement.objects.all()
    #serializer_class = AgreementSerializer

    def get_serializer_class(self):
        if self.request.method == 'PUT' or self.request.method == 'POST':
            return AgreementUpdateSerializer
        return AgreementSerializer


def generate_files(request, agreement_id):
    agreement = Agreement.objects.get(pk=agreement_id)
    print(agreement)
    manager = DocManager('SOZLESME_TEMPLATE.docx')
    filepath = manager.create(agreement)
    print('filepath', filepath)
    file = AgreementFile(agreement=agreement, file=filepath)
    file.save()
    print('file.file.path', file.file.path)
    return JsonResponse({'status': 1})
