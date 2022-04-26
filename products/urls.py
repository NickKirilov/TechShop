from django.urls import path
from products.views import ProductDetail, LatestProductList

urlpatterns = [
    path('latest-products/', LatestProductList.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>', ProductDetail.as_view()),
]