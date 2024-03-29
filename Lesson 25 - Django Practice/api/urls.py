from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import *
from .views import ProductView, ProductSingleView, CategoryProductsView, OrderView, OrderSingleView

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'v1/products', ProductViewSet, basename="api_products")
router.register(r'v1/categories', CategoryViewSet, basename="api_categories")
router.register(r'v1/orders', OrderViewSet, basename="api_orders")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path("v2/products/", ProductView.as_view()),
    path("v2/products/<int:id>", ProductSingleView.as_view()),
    path("v1/categories/<int:category_id>/products", CategoryProductsView.as_view()),
    path("v1/orders/<int:id>/items", OrderView.as_view()),
    path("v1/orders/<int:id>", OrderSingleView.as_view()),
]