
from django.urls import path,include
from . import views

urlpatterns = [
    path('reg/',views.register ,name="st" ),
   path('login/',views.login,name="signin"),
   
   path('sucess/',views.sucess,name="sucess"),
   
    
]