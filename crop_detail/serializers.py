from rest_framework import serializers
from .models import *

class WheatSerializer(serializers.ModelSerializer):
    class Meta:
        model=Wheat
        fields="__all__"
        
class Sorghum_JowarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sorghum_Jowar
        fields="__all__"        

class Chickpeas_GramSerializer(serializers.ModelSerializer):
    class Meta:
        model=Chickpeas_Gram
        fields="__all__"      
class Red_GramSerializer(serializers.ModelSerializer):
    class Meta:
        model=Red_Gram
        fields="__all__"    

class Lentils_MasoorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Lentils_Masoor
        fields="__all__"      

class Groundnut_PeanutSerializer(serializers.ModelSerializer):
    class Meta:
        model=Groundnut_Peanut
        fields="__all__"      

    
class SunflowerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sunflower
        fields="__all__"      

class MustardSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mustard
        fields="__all__"      

class TomatoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tomato
        fields="__all__"      

class ChiliSerializer(serializers.ModelSerializer):
    class Meta:
        model=Chili
        fields="__all__"      

class BrinjalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Brinjal
        fields="__all__"      

class CarrotSerializer(serializers.ModelSerializer):
    class Meta:
        model=Carrot
        fields="__all__"    

class RadishSerializer(serializers.ModelSerializer):
    class Meta:
        model=Radish
        fields="__all__"    

class SpinachSerializer(serializers.ModelSerializer):
    class Meta:
        model=Spinach
        fields="__all__"   

class CorianderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Coriander
        fields="__all__"    

class FenugreekSerializer(serializers.ModelSerializer):
    class Meta:
        model=Fenugreek
        fields="__all__"    

