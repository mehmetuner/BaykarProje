from rest_framework import serializers
from IhaApp.models import IhaData,UserWindowIha,CustomUser
class IhaSerializer(serializers.ModelSerializer):
    class Meta:
        model=IhaData
        fields=('Id','Name','Stock','YearUnitFee','Currency','IsForRent','IsDelete')
        
                
class UserWindowIhaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWindowIha
        fields = ('Id', 'IhaId', 'PurpchaseDate', 'PurpchaseEndDate', 'PurpchaseQuantity', 'TotalFee', 'Currency')

class UserSerializer(serializers.ModelSerializer):
     class Meta:
        model = CustomUser
        fields = ('Id', 'Username', 'Password')
