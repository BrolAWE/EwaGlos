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
    path('index/<str:lang>', views.index, name="index_translate"),
    path('about/<str:lang>', views.about, name="about"),
    path('sections/<str:lang>', views.sections, name="sections"),
    path('subsections/<str:lang>/<str:pk>', views.subsections, name="subsections"),
    path('words/<str:lang>/<str:pk>', views.words, name="words"),
    path('word/<str:lang>/<str:pk>/<str:lan>', views.word, name="word"),
    path('search/<str:lang>', views.search, name='search'),
    path('api/section', views.SectionView.as_view(), name="sections_api"),
    path('api/subsection/', views.SubsectionView.as_view(), name="subsections_api"),
    path('api/words/<str:pk>', views.WordsView.as_view(), name="words_api"),
    path('api/word/<str:pk>/<str:lan>', views.WordView.as_view(), name="api_word"),
]
admin.site.site_header = "Дроблин"
admin.site.site_title = "Admin"
admin.site.index_title = "EwaGlos"

