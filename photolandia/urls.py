from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('albums/', include('albums.urls')),
    path('photos/', include('photos.urls')),
    path('admin/', admin.site.urls),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, {'template_name': 'account/logout.html'}, name='logout'),
    path('api/login', views.api_login, name="api_login"),
    path('', views.IndexView.as_view()),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
