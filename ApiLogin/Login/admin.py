from django.contrib import admin
from  .models import  Techincals,Customers,User,Admin,orders,Devices,CustomerProfile,TechincalProfile
# Register your models here.


admin.site.register(Techincals)
admin.site.register(Customers)
admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Devices)
admin.site.register(orders)
admin.site.register(CustomerProfile)
admin.site.register(TechincalProfile)



