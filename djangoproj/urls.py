
from django.contrib import admin
from django.urls import path
from . import views
from auapp.views import uhome,usignup,uwelcome,ulogout,urnp
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path("uhome",uhome,name="uhome"),
    path("usignup",usignup,name="usignup"),
    path("uwelcome",uwelcome,name="uwelcome"),
    path("ulogout",ulogout,name="ulogout"),
    path("urnp",urnp,name="urnp"),
]
