from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register('agreements', views.AgreementViewSet, 'agreements')

urlpatterns = [
    path('tenants/', views.TenantListView.as_view(), name='tenants'),
    path('tenants/<int:pk>/', views.TenantRetrieveView.as_view(), name='tenant_details'),
    path('guarantors/', views.GuarantorListView.as_view(), name='guarantors'),
    path('guarantors/<int:pk>/', views.GuarantorRetrieveView.as_view(), name='guarantor_details'),
    path('landlords/', views.LandlordListView.as_view(), name='landlords'),
    path('landlords/<int:pk>/', views.LandlordRetrieveUpdateView.as_view(), name='landlord_edits'),
    path('rooms/', views.RoomListView.as_view(), name='rooms'),
    path('rooms/<int:pk>/', views.RoomRetrieveView.as_view(), name='room_details'),
    url(r'^', include(router.urls)),
    path('agreements/<int:agreement_id>/file', views.generate_files, name='agreements'),
]
