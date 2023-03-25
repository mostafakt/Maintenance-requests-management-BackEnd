from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework.authtoken.models import Token
from  rest_framework import serializers
from .models import Techincals,Customers,Admin,CustomerProfile,TechincalProfile,orders,Devices,mancontact


class CustomersRegistrationSerializer(RegisterSerializer):
    customer = serializers.PrimaryKeyRelatedField(read_only=True, )  # by default allow_null = False


    def get_cleaned_data(self):
        data = super(CustomersRegistrationSerializer, self).get_cleaned_data()
        extra_data = {

        }
        data.update(extra_data)
        return data

    def save(self, request):
        user = super(CustomersRegistrationSerializer, self).save(request)
        user.is_customer = True
        user.save()
        customer = Customers(customer=user,

                           )
        customer.save()
        return user


class TechincalsBuyerCustomRegistrationSerializer(RegisterSerializer):
    techincal = serializers.PrimaryKeyRelatedField(read_only=True, )  # by default allow_null = False

    def get_cleaned_data(self):
        data = super(TechincalsBuyerCustomRegistrationSerializer, self).get_cleaned_data()
        extra_data = {
            'techincal': self.validated_data.get('is_techincal', ''),
            'customer': self.validated_data.get('is_customer', ''),
        }
        data.update(extra_data)
        return data

    def save(self, request):
        user = super(TechincalsBuyerCustomRegistrationSerializer, self).save(request)
        user.is_techincal = True
        user.save()
        techincal = Techincals(techincal=user, )
        techincal.save()
        return user




class AdminRegistrationSerializer(RegisterSerializer):
    admin = serializers.PrimaryKeyRelatedField(read_only=True, )  # by default allow_null = False
    # country = serializers.CharField(required=True)

    def get_cleaned_data(self):
        data = super(AdminRegistrationSerializer, self).get_cleaned_data()
        extra_data = {
            # 'country': self.validated_data.get('country', ''),
        }
        data.update(extra_data)
        return data

    def save(self, request):
        user = super(AdminRegistrationSerializer, self).save(request)
        user.is_admin = True
        user.save()
        admin = Admin(admin=user,
                           #order=self.cleaned_data.get('country')

                           )
        admin.save()
        return user



class CustomerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomerProfile
        fields=('id','customer','companname','manager','technicalmanger','address','phonenumber','managermobile','email','website','facebook','serialnumber','logo')



class TechincalProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=TechincalProfile
        fields=('id','techincal','identityimage','name','domin','phonenumber','address')



class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=orders
        fields=('id', 'ordernumber' ,'customer' ,'techincal','name','description','problemimage','timeofoccurrance','Frequencyofoccurane','RequriedVisit','location')





class DevicesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Devices
        fields=('id','oredr' ,'name','serialnumber','deviceimage','devicemodel','type','workrate')








class mancontatSerizaizer(serializers.ModelSerializer):
    class Meta:
        model=mancontact
        fields=('id','name','techincal','telephone','email')




from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView






