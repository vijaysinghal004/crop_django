from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.generics import ListCreateAPIView

crop_detail={
     
    "Wheat" : "https://wholegrainscouncil.org/sites/default/files/thumbnails/image/15616367_ml-wheat-field.jpg" ,
    "Tomato": "https://th.bing.com/th/id/OIP.Txax4eLyujqla_fne8SGDgHaHa?pid=ImgDet&w=197&h=197&c=7&dpr=1.3",
    "Sunflower": "https://th.bing.com/th/id/OIP.wJyCVafSAZ6UbuKnqH_djgHaFb?w=237&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7",  
    "Chili": "https://th.bing.com/th/id/OIP.-3TkEptPXiEhDNrTzcIwkgHaHa?pid=ImgDet&w=197&h=197&c=7&dpr=1.3",
    "Radish": "https://th.bing.com/th/id/OIP.OT2duRDKsrMm1F9QciGZjgHaE8?w=299&h=199&c=7&r=0&o=5&dpr=1.3&pid=1.7",
    "Spinach": "https://th.bing.com/th/id/OIP.ZEExQwDJas8xRakAd95-RwHaFW?w=235&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7",
    "Chickpeas": "https://th.bing.com/th/id/OIP.UOiOTl068O4ULofTEYFtDQHaE8?pid=ImgDet&w=197&h=131&c=7&dpr=1.3",
    "Red_Gram": "https://th.bing.com/th/id/OIP.0CF0yttHYZ5hC0vXr9GpuAHaEL?w=292&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7",
    "Lentils": "https://th.bing.com/th/id/OIP.1H-YQEfTXwzTbS6xwgWdHAAAAA?w=281&h=187&c=7&r=0&o=5&dpr=1.3&pid=1.7",
    "Groundnut":"https://th.bing.com/th/id/OIP.loZvwv2LQksC8XF4icRWHgHaE1?w=254&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7",
    "Sorghum": "https://th.bing.com/th/id/OIP.AidvBEJ9y9dvZ-GELcj5gwHaFi?w=528&h=395&rs=1&pid=ImgDetMain",
    "Mustard": "https://th.bing.com/th/id/OIP.LsGZK-xZQL3NgOsUck-k_wHaFj?w=234&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7",
    "Brinjal": "https://th.bing.com/th/id/OIP.ZV7yoJBVtZPmjQ8U9c4VXAHaEJ?w=300&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7",
    "Carrot": "https://th.bing.com/th/id/OIP.uWkKdu7QOLRjHML1d53IDwHaHa?pid=ImgDet&w=197&h=197&c=7&dpr=1.3", 
    "Fenugreek": "https://th.bing.com/th/id/OIP.Gju9uQCHTYJ0FTuKwqbVRgHaFj?pid=ImgDet&w=197&h=147&c=7&dpr=1.3",
    "Coriander": "https://thumbs.dreamstime.com/b/coriander-crop-green-fresh-vegetable-field-soil-culture-agriculture-coriander-crop-green-vegetable-field-soil-culture-agriculture-108862119.jpg"
    
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


