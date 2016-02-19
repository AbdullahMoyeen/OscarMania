from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.PollsView.as_view(), name='polls'),
    url(r'^results/$', views.ResultsView.as_view(), name='results'),
    url(r'^vote/(?P<best_picture_nominee_id>\d+)$', views.VoteForBestPicture, name='vote'),
]
