from django.contrib import admin
from django.urls import path
from internationaleregler import views
urlpatterns = [
    path('', views.home, name="home"),
    path('drengene/', views.drengene, name="drengene"),
    path('racismelisten/', views.RacismPointListView.as_view(), name="racismelisten"),
    path('racismelisten/create', views.RacismPointCreateView.as_view(), name="racismelisten-create"),
]
