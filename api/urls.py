from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('predict/', views.predict, name='predict'),
   ## path('cultativetips',views.suggestation, name='suggestation')
]
