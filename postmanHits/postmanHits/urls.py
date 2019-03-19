"""postmanHits URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from api_1.resources import HitsResource
from api_2.resources import NoteResource
from api_1.views import homepage_view
from api_1.views import api_1_homepage_view
from api_2.views import api_2_homepage_view


hits_resource = HitsResource()
note_resource = NoteResource()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api_1/', include(hits_resource.urls)),
    url(r'^api_2/', include(note_resource.urls)),
    url(r'^$', homepage_view),
    url(r'api_1/$', api_1_homepage_view),
    url(r'api_2/$', api_2_homepage_view),
]
