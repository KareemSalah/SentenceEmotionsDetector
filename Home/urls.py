from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='Home.index'),
    url(r'^train/$', views.train, name='Home.train'),
    url(r'^predict/$', views.predict, name="Home.predict"),
]
