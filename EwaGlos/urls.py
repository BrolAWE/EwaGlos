"""EwaGlos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('sections', views.sections, name="sections"),
    path('subsections/<int:pk>', views.subsections, name="subsections"),
    path('words/<int:pk>', views.words, name="words"),
    path('word/<int:pk>/<str:lan>', views.word, name="word"),
    path('api/sections', views.SectionsView.as_view(), name="sections_api"),
    path('api/subsections/<int:pk>', views.SubsectionsView.as_view(), name="subsections_api"),
    path('api/words/<int:pk>', views.WordsView.as_view(), name="words_api"),
]
