from rest_framework import serializers

from .models import Announcement, Category, Subcategory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = '__all__'


class AnnouncementDetailSerializer(serializers.ModelSerializer):
    subcategory = serializers.SlugRelatedField(slug_field='title', read_only=True)
    discount = serializers.SerializerMethodField()

    def get_discount(self, obj):
        discount_of_price = float(obj.price) * 0.1
        return discount_of_price

    class Meta:
        model = Announcement
        fields = '__all__'


class AnnouncementSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    def get_category(self, obj):
        return obj.subcategory.category.title

    class Meta:
        model = Announcement
        fields = '__all__'