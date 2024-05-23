import re
from unicodedata import category
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer, CategoryDetailSerializer, ProductDetailSerializer, ReviewDetailSerializer, ProductReviewsSerializer

import product
from .models import Category, Product, Review

@api_view(['GET', 'POST'])
def product_list_api_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        list_ = ProductSerializer(products, many=True).data
        
        return Response(data=list_, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        price = request.data.get('price')
        category_id = request.data.get('category_id')
        
        product = Product.objects.create(
            title=title,
            description=description,
            price=price,
            category_id=category_id
        )
        return Response(status=status.HTTP_201_CREATED, data=ProductDetailSerializer(product).data)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'The specified category does not exist 🤔'})
    
    if request.method == 'GET':
        
        list_ = ProductDetailSerializer(product).data
        return Response(data=list_, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        product.title = request.data.get('title')
        product.description = request.data.get('description')
        product.price = request.data.get('price')
        product.category_id = request.data.get('category_id')
        
        product.save()
        
        return Response(status=status.HTTP_201_CREATED, data=ProductDetailSerializer(product).data)
   
    elif request.method == 'DELETE':
        product.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def category_list_api_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        list_ = CategorySerializer(categories, many=True).data
        
        return Response(data=list_, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        name = request.data.get('name')
        
        category = Category.objects.create(
            name=name
        )
    
    return Response(status=status.HTTP_201_CREATED, data=CategoryDetailSerializer(category).data)

@api_view(['GET', 'PUT', 'DELETE'])
def category_detail_api_view(request, id):
    try:
        category_ = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'There is no such categories!!!'})
    
    if request.method == 'GET':
        
        category_dict = CategoryDetailSerializer(category_).data
        
        return Response(data=category_dict)
    
    elif request.method == 'PUT':
        
        category_.name = request.data.get('name')
        
        category_.save()
        
        return Response(status=status.HTTP_201_CREATED, data=CategoryDetailSerializer(category_).data)
    
    elif request.method == 'DELETE':
        
        category_.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)  


@api_view(['GET', 'POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        
        reviews = Review.objects.all()
        
        list_ = ReviewSerializer(reviews, many=True).data
        
        return Response(data=list_, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        
        text = request.data.get('text')
        stars = request.data.get('stars')
        product_id = request.data.get('product_id')
        
        review = Review.objects.create(
            text=text,
            stars=stars,
            product_id=product_id
            
        )
        
    return Response(status=status.HTTP_201_CREATED, data=ReviewDetailSerializer(review).data)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, id):
    try:
        reviews = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'Unfortunately there is no such review 🤗'})
    
    if request.method == 'GET':
        list_ = ReviewDetailSerializer(reviews).data
        return Response(data=list_, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        reviews.text = request.data.get('text')
        reviews.product_id = request.data.get('product_id')
        reviews.stars = request.data.get('stars')
        
        reviews.save()
        
        return Response(status=status.HTTP_201_CREATED, data=ReviewDetailSerializer(reviews).data)
    
    elif request.method == 'DELETE':
        
        reviews.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def product_review_api_view(request):
    
    reviews = Review.objects.all()
    
    list_ = ProductDetailSerializer(reviews, many=True).data
    
    return Response(data=list_, status=status.HTTP_200_OK)


@api_view(['GET'])
def product_reviews_list_api_view(request):
    
    products = Product.objects.prefetch_related('reviews').all()
    
    serializer = ProductReviewsSerializer(products, many=True).data
    
    return Response(data=serializer, status=status.HTTP_200_OK)