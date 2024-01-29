from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_data, name="get_data"),
    path('addData/<int:id>', views.addData, name="addData"),
]
