"""
URL configuration for shop_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from product import views
from rest_framework.routers import DefaultRouter
from product.views import ProductModelViewSet, CategoryModelViewSet, ReviewModelViewSet, ProductDetailAPIView, \
                          CategoryDetailAPIView, ReviewDetailAPIView, ProductReviewsListAPIView



# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/v1/categories/', views.category_list_api_view),
#     path('api/v1/categories/<int:id>/', views.category_detail_api_view),
    
#     path('api/v1/products/', views.product_list_api_view),
#     path('api/v1/products/<int:id>/', views.product_detail_api_view),
#     path('api/v1/products/reviews/', views.product_reviews_list_api_view),
    
#     path('api/v1/reviews/', views.review_list_api_view),
#     path('api/v1/reviews/<int:id>/', views.review_detail_api_view),
    
#     path('api/v1/users/', include('users.urls'))
# ]


router = DefaultRouter()
router.register(r'products', ProductModelViewSet, basename='product')
router.register(r'categories', CategoryModelViewSet, basename='category')
router.register(r'reviews', ReviewModelViewSet, basename='review')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/products/<int:id>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('api/v1/categories/<int:id>/', CategoryDetailAPIView.as_view(), name='category-detail'),
    path('api/v1/products/reviews/', ProductReviewsListAPIView.as_view(), name='product-reviews-list'),
    path('api/v1/reviews/<int:id>/', ReviewDetailAPIView.as_view(), name='review-detail'),
    path('api/v1/users/', include('users.urls')),
]