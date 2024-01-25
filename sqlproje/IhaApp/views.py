from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from IhaApp.models import IhaData, UserWindowIha, CustomUser
from datetime import datetime

from IhaApp.serializers import IhaSerializer, UserWindowIhaSerializer, UserSerializer

loginsuccess = 0
ForIs_Admin = 0


@csrf_exempt
def ApiIha(request, id=0):
    global loginsuccess
    global ForIs_Admin
    if loginsuccess == 1 and ForIs_Admin == 1:
        if request.method == "GET":
            Iha_Data = IhaData.objects.filter(IsDelete=0)
            Iha_serializer = IhaSerializer(Iha_Data, many=True)
            return JsonResponse(Iha_serializer.data, safe=False)
        elif request.method == "POST":
            Iha_Data = JSONParser().parse(request)
            Iha_serializer = IhaSerializer(data=Iha_Data)
            if Iha_serializer.is_valid():
                Iha_serializer.save()
                return JsonResponse("Ekleme Başarılı! ", safe=False)
            return JsonResponse("Ekleme Hatalı!", safe=False)
        elif request.method == "PUT":
            Iha_Data = JSONParser().parse(request)
            Iha = IhaData.objects.get(Id=id)
            Iha_serializer = IhaSerializer(Iha, data=Iha_Data)
            if Iha_serializer.is_valid():
                Iha_serializer.save()
                return JsonResponse("Güncelleme Başarılı!", safe=False)
            return JsonResponse("Ekleme Hatalı!", safe=False)
        elif request.method == "DELETE":
            Iha = IhaData.objects.get(Id=id)
            Iha.delete()
            return JsonResponse("Silinme Başarılı!", safe=False)
    else:
        return JsonResponse("Giriş yapın ve Admin değilsiniz!", safe=False)


@csrf_exempt
def ApiUserWindowIha(request, id=0):
    global loginsuccess
    if loginsuccess == 1:
        if request.method == "GET":
            UserIha_Data = UserWindowIha.objects.all()
            UserIha_serializer = UserWindowIhaSerializer(UserIha_Data, many=True)
            return JsonResponse(UserIha_serializer.data, safe=False)

        elif request.method == "POST":
            UserIha_Data = JSONParser().parse(request)
            UserIha_Data["PurpchaseEndDate"] = int(UserIha_Data["PurpchaseEndDate"])
            UserIha_serializer = UserWindowIhaSerializer(data=UserIha_Data)
            if UserIha_serializer.is_valid():
                stock_iha = IhaData.objects.get(Id=UserIha_Data["IhaId"])
                stock_iha.Stock -= int(UserIha_Data["PurpchaseQuantity"])
                stock_iha.save()
                durationCalculate = int(UserIha_Data["PurpchaseEndDate"]) - int(
                    datetime.now().year
                )
                YearUnitFee = stock_iha.YearUnitFee
                Fee = (
                    YearUnitFee
                    * float(durationCalculate)
                    * (float(UserIha_Data["PurpchaseQuantity"]))
                )
                UserIha_serializer.validated_data["TotalFee"] = Fee
                UserIha_serializer.save()
                return JsonResponse("Ekleme Başarılı!", safe=False)
            return JsonResponse("Ekleme Hatalı!", safe=False)
    else:
        return JsonResponse("Giriş yapın!", safe=False)


@csrf_exempt
def user_login(request, id=0):
    global loginsuccess
    global ForIs_Admin
    if request.method == "POST":
        User_Data = JSONParser().parse(request)
        User_serializer = UserSerializer(data=User_Data)
        if User_serializer.is_valid():
            username = User_Data.get("Username", None)
            password = User_Data.get("Password", None)

            try:
                user = CustomUser.objects.get(Username=username, Password=password)
                loginsuccess = 1
                ForIs_Admin = user.Is_Admin
                return JsonResponse("Giriş başarılı!", safe=False)
            except CustomUser.DoesNotExist:
                return JsonResponse("Kullanıcı adın veya şifren yanlış!", safe=False)
        else:
            return JsonResponse("Hata", safe=False)
