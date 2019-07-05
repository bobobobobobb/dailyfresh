from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<book_id>\d+)/$', views.HeroinfoView.as_view()),

]

