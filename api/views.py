from django.http import JsonResponse
from rest_framework import generics, viewsets

from api.doc_manager.manager import DocManager
from api.models import Tenant, Guarantor, Landlord, Room, Agreement, AgreementFile
from api.serializers import TenantSerializer, GuarantorSerializer, LandlordSerializer, RoomSerializer, \
    AgreementSerializer, RoomUpdateSerializer


class TenantListView(generics.ListAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer

class TenantRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer

class GuarantorListView(generics.ListAPIView):
    queryset = Guarantor.objects.all()
    serializer_class = GuarantorSerializer

class GuarantorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guarantor.objects.all()
    serializer_class = GuarantorSerializer


class LandlordListView(generics.ListAPIView):
    queryset = Landlord.objects.all()
    serializer_class = LandlordSerializer

class LandlordRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Landlord.objects.all()
    serializer_class = LandlordSerializer

class RoomListView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class RoomRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    #serializer_class = RoomUpdateSerializer

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return RoomUpdateSerializer 
        return RoomSerializer 

class BaseViewSet(viewsets.ModelViewSet):    # TODO: add permissions here
    pass

class AgreementViewSet(BaseViewSet):
    queryset = Agreement.objects.all()
    serializer_class = AgreementSerializer


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
