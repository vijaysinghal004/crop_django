from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.generics import ListCreateAPIView

crop_detail={
    "Weat":"lgwiegule"
}

class CropDetail(APIView):
    def get(self,request):
        response = []
        for key,value in crop_detail.items():
            response.append({
                "crop_name": key,
                "image_url": value
            })
        return Response({  "Crops": response, "success" :True}
        )


class WheatView(ListCreateAPIView):
    queryset=Wheat.objects.all()
    serializer_class=WheatSerializer

class Sorghum_JowarView(ListCreateAPIView):
    queryset=Sorghum_Jowar.objects.all()
    serializer_class=Sorghum_JowarSerializer

class Chickpeas_GramView(ListCreateAPIView):
    queryset=Chickpeas_Gram.objects.all()
    serializer_class=Chickpeas_GramSerializer

class Red_GramView(ListCreateAPIView):
    queryset=Red_Gram.objects.all()
    serializer_class=Red_GramSerializer

class Lentils_MasoorView(ListCreateAPIView):
    queryset=Lentils_Masoor.objects.all()
    serializer_class=Lentils_MasoorSerializer

class Groundnut_PeanutView(ListCreateAPIView):
    queryset=Groundnut_Peanut.objects.all()
    serializer_class=Groundnut_PeanutSerializer

class SunflowerView(ListCreateAPIView):
    queryset=Sunflower.objects.all()
    serializer_class=SunflowerSerializer

class MustardView(ListCreateAPIView):
    queryset=Mustard.objects.all()
    serializer_class=MustardSerializer

class TomatoView(ListCreateAPIView):
    queryset=Tomato.objects.all()
    serializer_class=TomatoSerializer

class ChiliView(ListCreateAPIView):
    queryset=Chili.objects.all()
    serializer_class=ChiliSerializer

class BrinjalView(ListCreateAPIView):
    queryset=Brinjal.objects.all()
    serializer_class=BrinjalSerializer

class CarrotView(ListCreateAPIView):
    queryset=Carrot.objects.all()
    serializer_class=CarrotSerializer

class RadishView(ListCreateAPIView):
    queryset=Radish.objects.all()
    serializer_class=RadishSerializer

class SpinachView(ListCreateAPIView):
    queryset=Spinach.objects.all()
    serializer_class=SpinachSerializer

class CorianderView(ListCreateAPIView):
    queryset=Coriander.objects.all()
    serializer_class=CorianderSerializer

class FenugreekView(ListCreateAPIView):
    queryset=Fenugreek.objects.all()
    serializer_class=FenugreekSerializer


