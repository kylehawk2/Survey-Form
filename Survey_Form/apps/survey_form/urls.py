from django.conf.urls import url
from . import views
urlpatterns =[
    url(r'^$', views.index),
    url(r'^postinfo$', views.postinfo),
    url(r'^result$', views.result),
]