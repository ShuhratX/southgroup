from django.urls import path
from .views import *

urlpatterns = [
    path('category/', CategoryView.as_view()),
    path('category/<int:pk>/', CategoryDetailView.as_view()),
    path('product/', ProductView.as_view()),
    path('product/<int:pk>/', ProductDetailView.as_view()),

]