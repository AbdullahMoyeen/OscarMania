from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/$', views.HomeView.as_view(), name='home'),
    url(r'^results/$', views.ResultsView.as_view(), name='results'),
    url(r'^vote/(?P<best_picture_nominee_id>\d+)$', views.VoteForBestPicture, name='vote'),
]
