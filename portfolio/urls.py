from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from homepage.views import HomePageView, SuccessPageView

urlpatterns = [
    # Admin Page
    path('admin/', admin.site.urls),
    # Home Page
    path('', HomePageView.as_view()),
    # Success page
    path('success', SuccessPageView.as_view())
]
# Static files urls
urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Media files urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
