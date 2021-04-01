from django.urls import path
from . import views
from django.conf.urls.static import static
app_name='comp'

urlpatterns = [
    path('Home/',views.Home,name='Home'),
    path('about/',views.about,name='about'),
    path('contactus/',views.contactus,name='contactus'),
]