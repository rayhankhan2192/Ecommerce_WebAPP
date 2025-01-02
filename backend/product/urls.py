from django.urls import path
from product import views

urlpatterns = [
    path('create/', views.ProductsListView.as_view(), name="product_list"),
    path('all-products/', views.ProductsListView.as_view()),
    path('<slug:category_slug>/<slug:product_slug>/', views.ProductDetailsView.as_view()),
    
]
