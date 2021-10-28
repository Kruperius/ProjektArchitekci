"""Architekci URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Architekt import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.strona_gl),
    path('architekci/', views.architekci),
    path('projekty/', views.projekty),
    path('dodaj-architekta/', views.dodaj_architekta),
    path('dodaj-projekt/', views.dodaj_projekt),
    path('zaktualizuj-projekt/<str:pk>/', views.update_projekt, name='update_projekt'),
    path('usun-projekt/<str:pk>/', views.delete_projekt, name='delete_projekt'),
    # path(r'^signup/$', views.signup, name='signup'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('login/', views.signin),
    path('logout/', views.signout),
    path('konta/', include('django.contrib.auth.urls')),
    path('mojeprojekty/', views.ProjektyByUserListView.as_view(), name='moje-projekty')
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
