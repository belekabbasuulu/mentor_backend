from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Announcement, Category, Subcategory
from .serializers import (
    AnnouncementListSerializer,
    AnnouncementCreateSerializer,
    AnnouncementRetrieveSerializer,
    AnnouncementSerializer,
    CategorySerializer,
    SubcategorySerializer
)

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubcategoryViewSet(ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer


class AnnouncementViewSet(ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

    


# class MentorView(APIView):
#     def get(self, request, *args, **kwargs):
#         ads = Announcement.objects.all()
#         ads_json = AnnouncementListSerializer(ads, many=True)
#         return Response(ads_json.data, status=200)
    
#     def post(self, request):
#         data = request.data
#         serializer = AnnouncementCreateSerializer(data=data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=201)
    

# class AnnouncementRetrieveView(RetrieveAPIView):
#     queryset = Announcement.objects.all()
#     serializer_class = AnnouncementRetrieveSerializer


# class AnnouncementUpdateView(UpdateAPIView):
#     queryset = Announcement.objects.all()
#     serializer_class = AnnouncementSerializer


# class AnnouncementDeleteView(DestroyAPIView):
#     queryset = Announcement.objects.all()
#     serializer_class = AnnouncementSerializer


# class AnnouncementCreateView(CreateAPIView):
#     queryset = Announcement.objects.all()
#     serializer_class = AnnouncementSerializer


# class AnnouncementRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
#     queryset = Announcement.objects.all()
#     serializer_class = AnnouncementSerializer
