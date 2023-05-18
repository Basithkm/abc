from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.index,name='home'),
    path('about/',views.about,name='about'),
    path('features/',views.features,name='features'),
    path('pricing/',views.pricing,name='pricing'),
    path('trainers/',views.trainers,name='trainers'),
    path('blog/',views.blog,name='blog'),
]
