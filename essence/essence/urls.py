from django.contrib import admin
from django.urls import path
from mainApp import views as mainApp
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mainApp.home),
]
