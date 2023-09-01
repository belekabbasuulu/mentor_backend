from rest_framework import serializers

from .models import Announcement


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


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'