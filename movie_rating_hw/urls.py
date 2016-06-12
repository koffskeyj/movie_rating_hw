"""movie_rating_hw URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from movierating import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^movies/(?P<movie_id>\w+)/$', views.movie_index),
    url(r'^raters/(?P<rater_id>\w+)/$', views.rater_index),
    #url(r'^top20ratings/(?P<rating_id>\w+)/$', views.top20_rating_index)
    url(r'^top20ratings/$', views.top20_rating_index)
]
