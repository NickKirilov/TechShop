from django.urls import path
from products import views

urlpatterns = [
    path('latest-products/', views.LatestProductList.as_view()),
]