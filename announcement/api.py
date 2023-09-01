from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.response import Response

from .models import Announcement
from .serializers import (
    AnnouncementListSerializer,
    AnnouncementCreateSerializer,
    AnnouncementRetrieveSerializer,
    AnnouncementSerializer
)


class MentorView(APIView):
    def get(self, request, *args, **kwargs):
        ads = Announcement.objects.all()
        ads_json = AnnouncementListSerializer(ads, many=True)
        return Response(ads_json.data, status=200)
    
    def post(self, request):
        data = request.data
        serializer = AnnouncementCreateSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
    

class AnnouncementRetrieveView(RetrieveAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementRetrieveSerializer


class AnnouncementUpdateView(UpdateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer


class AnnouncementDeleteView(DestroyAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer


class AnnouncementCreateView(CreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
