from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register('agreements', views.AgreementViewSet, 'agreements')

urlpatterns = [
    path('tenants/', views.TenantListCreateView.as_view(), name='tenants'),
    path('tenants/<int:pk>/', views.TenantRetrieveUpdateDestroyView.as_view(), name='tenant_actions'),
    path('guarantors/', views.GuarantorListCreateView.as_view(), name='guarantors'),
    path('guarantors/<int:pk>/', views.GuarantorRetrieveUpdateDestroyView.as_view(), name='guarantor_actions'),
    path('landlords/', views.LandlordListCreateView.as_view(), name='landlords'),
    path('landlords/<int:pk>/', views.LandlordRetrieveUpdateDestroyView.as_view(), name='landlord_actions'),
    path('rooms/', views.RoomListCreateView.as_view(), name='rooms'),
    path('rooms/<int:pk>/', views.RoomRetrieveUpdateDestroyView.as_view(), name='room_actions'),
    url(r'^', include(router.urls)),
    path('agreements/<int:agreement_id>/create_files', views.generate_files, name='agreements'),
    path('issues/', views.IssueListCreateView.as_view(), name='issues'),
    path('coupons/', views.CouponListCreateView.as_view(), name='coupons'),
    path('coupons/<int:pk>/', views.CouponRetrieveUpdateDestroyView.as_view(), name='coupon_actions'),
    path('guarantors/<int:pk>/', views.IssueRetrieveUpdateDestroyView.as_view(), name='issue_actions'),
    path('issues/<int:pk>/', views.IssueRetrieveUpdateDestroyView.as_view(), name='issue_actions'),


]
