from django.urls import path
from . import views

urlpatterns = [
    path('cropDetail/', views.CropDetail.as_view(), name='CropDetail'),
    path('wheat/',views.WheatView.as_view()),
    path('Sorghum_Jowar/',views.Sorghum_JowarView.as_view()),
    path('Chickpeas_Gram/',views.Chickpeas_GramView.as_view()),
    path('Red_Gram/',views.Red_GramView.as_view()),
    path('Lentils_Masoor/',views.Lentils_MasoorView.as_view()),
    path('Groundnut_Peanut/',views.Groundnut_PeanutView.as_view()),
    path('Sunflower/',views.SunflowerView.as_view()),
    path('Mustard/',views.MustardView.as_view()),
    path('Tomato/',views.TomatoView.as_view()),
    path('Chili/',views.ChiliView.as_view()),
    path('Brinjal/',views.BrinjalView.as_view()),
    path('Carrot/',views.CarrotView.as_view()),
    path('Radish/',views.RadishView.as_view()),
    path('Spinach/',views.SpinachView.as_view()),
    path('Coriander/',views.CorianderView.as_view()),
    path('Fenugreekt/',views.FenugreekView.as_view()),
]
