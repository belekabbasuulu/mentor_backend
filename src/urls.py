from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from announcement.api import (
    MentorView,
    AnnouncementRetrieveView,
    AnnouncementUpdateView,
    AnnouncementDeleteView,
    AnnouncementCreateView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('announcements/', MentorView.as_view()),
    path('announcements-create/', AnnouncementCreateView.as_view()),
    path('announcements/<int:pk>/', AnnouncementRetrieveView.as_view()),
    path('announcements-update/<int:pk>/', AnnouncementUpdateView.as_view()),
    path('announcements-delete/<int:pk>/', AnnouncementDeleteView.as_view()),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
