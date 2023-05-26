from django.urls import path
from .views import ProductsAPIView

urlpatterns = [
    path('',ProductsAPIView.as_view()),
    # path('<int:pk>/', ProductSingleAPIView.as_view()),
    # path('filter/',FilterProductAPIView.as_view()),
    # path('category/',CategoryAPIView.as_view())
]