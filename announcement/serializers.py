from rest_framework import serializers

from .models import Announcement, Category, Subcategory


class AnnouncementListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ['id', 'title', 'description']


class AnnouncementCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ['title', 'description']


class AnnouncementRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = '__all__'


class AnnouncementSerializer(serializers.ModelSerializer):
    subcategory = serializers.SlugRelatedField(slug_field='title', read_only=True)
    discount = serializers.SerializerMethodField()

    def get_discount(self, obj):
        discount_of_price = float(obj.price) * 0.1
        return discount_of_price

    class Meta:
        model = Announcement
        fields = '__all__'