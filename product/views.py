
from unicodedata import category
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer, CategoryDetailSerializer, ProductDetailSerializer, \
                        ReviewDetailSerializer, ProductReviewsSerializer, CategoryValidateSerializer, ProductValidateSerializer, ReviewValidateSerializer

import product
from .models import Category, Product, Review

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination



class CustomPagination(PageNumberPagination):
    page_size = 5



class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.action in ['list', 'create']:
            return ProductValidateSerializer
        return ProductDetailSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})
        product = Product.objects.create(**serializer.validated_data)
        return Response(ProductDetailSerializer(product).data, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'POST'])
# def product_list_api_view(request):
#     if request.method == 'GET':
#         products = Product.objects.all()
#         list_ = ProductSerializer(products, many=True).data
        
#         return Response(data=list_, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
        
#         serializer = ProductValidateSerializer(data=request.data)
        
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
        
        
#         title = serializer.validated_data.get('title')
#         description = serializer.validated_data.get('description')
#         price = serializer.validated_data.get('price')
#         category_id = serializer.validated_data.get('category_id')
        
#         product = Product.objects.create(
#             title=title,
#             description=description,
#             price=price,
#             category_id=category_id
#         )
#         return Response(status=status.HTTP_201_CREATED, data=ProductDetailSerializer(product).data)

class ProductDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        product = self.get_object()
        serializer = ProductValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        for attr, value in serializer.validated_data.items():
            setattr(product, attr, value)
        product.save()
        return Response(ProductDetailSerializer(product).data, status=status.HTTP_200_OK)

# @api_view(['GET', 'PUT', 'DELETE'])
# def product_detail_api_view(request, id):
#     try:
#         product = Product.objects.get(id=id)
#     except Product.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND, data={'The specified category does not exist 🤔'})
    
#     if request.method == 'GET':
        
#         list_ = ProductDetailSerializer(product).data
#         return Response(data=list_, status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
        
#         serializer = ProductValidateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
        
#         product.title = serializer.validated_data.get('title')
#         product.description = serializer.validated_data.get('description')
#         product.price = serializer.validated_data.get('price')
#         product.category_id = serializer.validated_data.get('category_id')
#         product.save()
        
#         return Response(status=status.HTTP_201_CREATED, data=ProductDetailSerializer(product).data)
   
#     elif request.method == 'DELETE':
#         product.delete()
        
#         return Response(status=status.HTTP_204_NO_CONTENT)

class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CustomPagination
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.action in ['list', 'create']:
            return CategoryValidateSerializer
        return CategoryDetailSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})
        category = Category.objects.create(**serializer.validated_data)
        return Response(CategoryDetailSerializer(category).data, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'POST'])
# def category_list_api_view(request):
#     if request.method == 'GET':
#         categories = Category.objects.all()
#         list_ = CategorySerializer(categories, many=True).data
        
#         return Response(data=list_, status=status.HTTP_200_OK)
    
#     elif request.method == 'POST':
        
#         serializer = CategoryValidateSerializer(data=request.data)
        
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
        
#         name = serializer.validated_data.get('name')
        
#         category = Category.objects.create(
#             name=name
#         )
    
#     return Response(status=status.HTTP_201_CREATED, data=CategoryDetailSerializer(category).data)


class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        category = self.get_object()
        serializer = CategoryValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        category.name = serializer.validated_data.get('name')
        category.save()
        return Response(CategoryDetailSerializer(category).data, status=status.HTTP_200_OK)


# @api_view(['GET', 'PUT', 'DELETE'])
# def category_detail_api_view(request, id):
#     try:
#         category_ = Category.objects.get(id=id)
#     except Category.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND, data={'There is no such categories!!!'})
    
#     if request.method == 'GET':
        
#         category_dict = CategoryDetailSerializer(category_).data
        
#         return Response(data=category_dict)
    
#     elif request.method == 'PUT':
        
#         serializer = CategoryValidateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
        
#         category_.name = serializer.validated_data.get('name')
        
#         category_.save()
        
#         return Response(status=status.HTTP_201_CREATED, data=CategoryDetailSerializer(category_).data)
    
#     elif request.method == 'DELETE':
        
#         category_.delete()
        
#         return Response(status=status.HTTP_204_NO_CONTENT)  


class ReviewModelViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = CustomPagination
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.action in ['list', 'create']:
            return ReviewValidateSerializer
        return ReviewDetailSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})
        review = Review.objects.create(**serializer.validated_data)
        return Response(ReviewDetailSerializer(review).data, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'POST'])
# def review_list_api_view(request):
#     if request.method == 'GET':
        
#         reviews = Review.objects.all()
        
#         list_ = ReviewSerializer(reviews, many=True).data
        
#         return Response(data=list_, status=status.HTTP_200_OK)
    
#     elif request.method == 'POST':
        
#         serializer = ReviewValidateSerializer(data=request.data)
        
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
        
#         text = serializer.validated_data.get('text')
#         stars = serializer.validated_data.get('stars')
#         product_id = serializer.validated_data.get('product_id')
        
#         review = Review.objects.create(
#             text=text,
#             stars=stars,
#             product_id=product_id
            
#         )
        
#     return Response(status=status.HTTP_201_CREATED, data=ReviewDetailSerializer(review).data)


class ReviewDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewDetailSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        review = self.get_object()
        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        for attr, value in serializer.validated_data.items():
            setattr(review, attr, value)
        review.save()
        return Response(ReviewDetailSerializer(review).data, status=status.HTTP_200_OK)


# @api_view(['GET', 'PUT', 'DELETE'])
# def review_detail_api_view(request, id):
#     try:
#         reviews = Review.objects.get(id=id)
#     except Review.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND, data={'Unfortunately there is no such review 🤗'})
    
#     if request.method == 'GET':
#         list_ = ReviewDetailSerializer(reviews).data
#         return Response(data=list_, status=status.HTTP_200_OK)
    
#     elif request.method == 'PUT':
        
#         serializer = ReviewValidateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
        
#         reviews.text = serializer.validated_data.get('text')
#         reviews.product_id = serializer.validated_data.get('product_id')
#         reviews.stars = serializer.validated_data.get('stars')
#         reviews.save()
        
#         return Response(status=status.HTTP_201_CREATED, data=ReviewDetailSerializer(reviews).data)
    
#     elif request.method == 'DELETE':
        
#         reviews.delete()
        
#         return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET'])
# def product_review_api_view(request):
    
#     reviews = Review.objects.all()
    
#     list_ = ProductDetailSerializer(reviews, many=True).data
    
#     return Response(data=list_, status=status.HTTP_200_OK)



class ProductReviewsListAPIView(ListCreateAPIView):
    queryset = Product.objects.prefetch_related('reviews').all()
    serializer_class = ProductReviewsSerializer
    pagination_class = CustomPagination


# @api_view(['GET'])
# def product_reviews_list_api_view(request):
    
#     products = Product.objects.prefetch_related('reviews').all()
    
#     serializer = ProductReviewsSerializer(products, many=True).data
    
#     return Response(data=serializer, status=status.HTTP_200_OK)