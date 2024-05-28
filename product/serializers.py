from dataclasses import fields
from importlib.metadata import requires
from unicodedata import category
from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from .models import Category, Product, Review

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'name products_count'.split()


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'id name'.split()
        

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'title'.split()


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'id title description price category'.split()
        
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'product'.split()


class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text product'.split()
        

class ProductReviewsSerializer(serializers.ModelSerializer):
    reviews = ReviewDetailSerializer(many=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ' title reviews average_rating'.split()

    def get_average_rating(self, obj):
        reviews = obj.reviews.all()
        if reviews:
            return sum(review.stars for review in reviews) / len(reviews)
        return None
    

class CategoryValidateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=5)
    
       
class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=5)
    description = serializers.CharField(required=False)
    price = serializers.FloatField()
    category_id = serializers.IntegerField()
    
    
    def validate_category_id(self, category_id):
        
        try:
            Category.objects.get(id=category_id)
            
        except:
            raise ValidationError('There is no such category')
        
        return category_id
    
    
class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(required=False)
    product_id = serializers.IntegerField()
    stars = serializers.IntegerField(min_value=1, max_value=5)
    
    def validate_product_id(self, product_id):
        
        try:
            Product.objects.get(id=product_id)
        
        except:
            raise ValidationError('Sorry for such a product')
        
        return product_id