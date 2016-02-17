from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^oscars/2016/best-picture/', include('BestPicturePolls.urls'))
]
