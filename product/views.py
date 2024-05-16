from unicodedata import category
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer, CategoryDetailSerializer, ProductDetailSerializer, ReviewDetailSerializer

import product
from .models import Category, Product, Review

@api_view(['GET'])
def product_list_api_view(request):
    products = Product.objects.all()
    list_ = ProductSerializer(products, many=True).data
    
    return Response(data=list_, status=status.HTTP_200_OK)


@api_view(['GET'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'The specified category does not exist 🤔'})
    list_ = ProductDetailSerializer(product).data
    
    return Response(data=list_, status=status.HTTP_200_OK)


@api_view(['GET'])
def category_list_api_view(request):
    categories = Category.objects.all()
    list_ = CategorySerializer(categories, many=True).data
    
    return Response(data=list_, status=status.HTTP_200_OK)

@api_view(['GET'])
def category_detail_api_view(request, id):
    try:
        category_ = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'There is no such categories!!!'})
    
    category_dict = CategoryDetailSerializer(category_).data
    
    return Response(data=category_dict)  


@api_view(['GET'])
def review_list_api_view(request):
    reviews = Review.objects.all()
    list_ = ReviewSerializer(reviews, many=True).data
    
    return Response(data=list_, status=status.HTTP_200_OK)


@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        reviews = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'Unfortunately there is no such review 🤗'})
    list_ = ReviewDetailSerializer(reviews).data
    
    return Response(data=list_, status=status.HTTP_200_OK)