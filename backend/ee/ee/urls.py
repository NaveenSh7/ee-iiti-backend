from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.http import JsonResponse

def healthz(_request):
    return JsonResponse({"status": "ok"})

def ping(_request):
    return JsonResponse({"ok": True})

urlpatterns = [
    path("iiti-ee-admin-login/", admin.site.urls),
    path("api/announcement/", include('announcements.urls'), name="announcement"),
    path("api/events/", include('events.urls'), name='event'),
    path("api/news/", include('news.urls'), name='news'),
    path("api/people/", include('people.urls'), name='people'),
    path("api/research/", include('research.urls'), name='research'),
    path("api/course/", include('course.urls'), name='course'),
    path("api/achievements/", include('achievements.urls'), name='achievements'),
    path("api/banana/", include('banana.urls'), name='banana'),
    path("api/reads/",include('reads.urls'),name='read'),
    path("admin/", admin.site.urls),
    path("healthz", healthz),  # GET https://ee-iiti.onrender.com/healthz
    path("api/ping", ping),    # GET https://ee-iiti.onrender.com/api/ping
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
