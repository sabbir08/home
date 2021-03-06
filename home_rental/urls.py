"""home_rental URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
admin.site.site_header = "Admin Panel "

urlpatterns = [
    path('', include("index.urls"),name="index"),
    path('flats/', include("flats.urls"),name="flats"),
    path('house/', include("houses.urls"),name="house"),
    path('accounts/', include("accounts.urls"),name="accounts"),
    path('dashboard/', include("dashboard.urls"),name="dashboard"),
    path('reservation/', include("reservations.urls"),name="reservation"),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
