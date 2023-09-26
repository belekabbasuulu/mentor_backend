from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
   openapi.Info(
      title="MENTOR Backend API",
      default_version='v1',
      description="APIs description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   authentication_classes=(SessionAuthentication,),
   permission_classes=(permissions.IsAuthenticated,),
)

urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    path('admin/', admin.site.urls),
    path('api/v1/announcements/', include('announcement.urls')),
    path('api/v1/users/', include('users.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('announcements/', MentorView.as_view()),
    # path('announcements/<int:pk>/', AnnouncementRetrieveUpdateDestroyView.as_view()),
    # path('announcements-create/', AnnouncementCreateView.as_view()),
    # path('announcements/<int:pk>/', AnnouncementRetrieveView.as_view()),
    # path('announcements-update/<int:pk>/', AnnouncementUpdateView.as_view()),
    # path('announcements-delete/<int:pk>/', AnnouncementDeleteView.as_view()),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
