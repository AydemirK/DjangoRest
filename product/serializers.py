from dataclasses import fields
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