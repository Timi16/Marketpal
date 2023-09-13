from django.urls import path
from .views import FarmerDetailView, BuyerDetailView,FarmerProductDetailView,FarmerProductView,ProductListView,BuyerProductSearchView
urlpatterns = [
    path('farmers/<int:pk>/', FarmerDetailView.as_view(), name='farmer'),
    path('buyers/<int:pk>/',BuyerDetailView.as_view(), name='buyer'),
    path("farmersproduct/<int:pk>/",FarmerProductDetailView.as_view(),name='farmersproduct'),
    path("farmersproductlist/",FarmerProductView.as_view(),name="farmersproductlist"),
    path("products/",ProductListView.as_view(),name="products"),
    path("products/search",BuyerProductSearchView.as_view(),name="product-search")
]
