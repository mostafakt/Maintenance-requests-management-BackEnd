from django.contrib import admin
from django.urls import path,include
from .views import TechincalsRegistrationView, CustomersRegistrationView,AdminRegistrationView,CustomerProfileViewSet,TechincalProfileViewSet,OrderViewSet,DevicesViewSet
from rest_framework import routers
from .views import MancontactViewset ,MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt import views as jwt_views


router=routers.DefaultRouter()

router.register('CustomerProfile',CustomerProfileViewSet,basename='CustomerProfile')
router.register('TechincalProfile',TechincalProfileViewSet,basename='Techincal')
router.register('Devices',DevicesViewSet,basename='device')
router.register('orders',OrderViewSet,basename='order')
router.register('man',MancontactViewset,basename='man')


urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('registration/customer/', CustomersRegistrationView.as_view(), name='register-seller'),
    path('registration/tech/', TechincalsRegistrationView.as_view(), name='register-buyer'),
    path('registration/admin/', AdminRegistrationView.as_view(), name='register-admin'),
    path('router', include(router.urls)),



]