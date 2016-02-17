from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^', views.HomeView.as_view(), name='home'),
    url(r'^vote/(?P<best_picture_nominee_id>\d+)$', views.VoteForBestPicture, name='vote'),
]
