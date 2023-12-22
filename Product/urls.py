from django.urls import path
from .views import CreateCategory, UpdateCategory, ListCategory, DeleteCategory, ListProduct, CreateProduct, UpdateProduct, DeleteProduct, ProductByCategory, ProductDetails

urlpatterns = [
    path('category', ListCategory.as_view(), name="ListCategory"),
    path('category/create', CreateCategory.as_view(), name="CreateCategory"),
    path('<int:pk>/category/update', UpdateCategory.as_view(), name="UpdateCategory"),
    path('<int:pk>/category/delete', DeleteCategory.as_view(), name="DeleteCategory"),
    path('product', ListProduct.as_view(), name="ListProduct"),
    path('<int:pk>/detail', ProductDetails.as_view(), name="ProductDetails"),
    path('product/<int:category>', ProductByCategory.as_view(), name="ProductByCategory"),
    path('product/create', CreateProduct.as_view(), name="CreateProduct"),
    path('<int:pk>/product/update', UpdateProduct.as_view(), name="UpdateProduct"),
    path('<int:pk>/product/delete', DeleteProduct.as_view(), name="DeleteProduct"),
]
