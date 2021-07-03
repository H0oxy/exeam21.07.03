from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls', namespace='main')),
    path('about_us/', include('mainapp.urls', namespace='about_us')),
    path('login/', include('mainapp.urls', namespace='login')),
]
