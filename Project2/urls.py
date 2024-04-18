
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app2/', include('app2.urls')),
]

urlpatterns += staticfiles_urlpatterns()