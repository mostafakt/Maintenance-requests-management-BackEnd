from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_auth.registration.views import RegisterView
from .models import CustomerProfile,TechincalProfile,orders,Devices
from .models import mancontact,image_orders
from rest_framework import viewsets
from .serializers import CustomerProfileSerializer,TechincalProfileSerializer,DevicesSerializer,OrderSerializer
from .serializers import mancontatSerizaizer,problemOrderimageSerializer

from .serializers import (
    CustomersRegistrationSerializer, TechincalsBuyerCustomRegistrationSerializer,
    AdminRegistrationSerializer
    )
app_name = 'Login'


class CustomersRegistrationView(RegisterView):
    serializer_class = CustomersRegistrationSerializer


class TechincalsRegistrationView(RegisterView):
    serializer_class = TechincalsBuyerCustomRegistrationSerializer



class AdminRegistrationView(RegisterView):
    serializer_class = AdminRegistrationSerializer



class CustomerProfileViewSet(viewsets.ModelViewSet):
    queryset = CustomerProfile.objects.all()
    serializer_class = CustomerProfileSerializer




class TechincalProfileViewSet(viewsets.ModelViewSet):
    queryset = TechincalProfile.objects.all()
    serializer_class = TechincalProfileSerializer



class MancontactViewset(viewsets.ModelViewSet):
    queryset = mancontact.objects.all()
    serializer_class = mancontatSerizaizer



class DevicesViewSet(viewsets.ModelViewSet):
    queryset = Devices.objects.all()
    serializer_class = DevicesSerializer



class OrderViewSet(viewsets.ModelViewSet):
    queryset = orders.objects.all()
    serializer_class = OrderSerializer



class ImageOrderProblemViewSet(viewsets.ModelViewSet):
    queryset = image_orders.objects.all()
    serializer_class = problemOrderimageSerializer



from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework_simplejwt.tokens import RefreshToken





class MyTokenObtainPairSerializers(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['is_techincal'] = user.is_techincal
        token['is_customer'] = user.is_customer
        token['is_admin'] = user.is_admin        # ...

        return token






class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializers