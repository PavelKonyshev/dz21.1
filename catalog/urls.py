from django.urls import path
from .apps import CatalogConfig
from .views import ProductListView, ProductDetailView, ContactPageView

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("contacts/", ContactPageView.as_view(), name="contacts"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_detail")
]
