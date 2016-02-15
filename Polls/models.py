from django.db import models


# Create your models here.

class BestPictureNominee(models.Model):
    best_picture_nominee_id = models.IntegerField
    create_user = models.CharField(max_length=50)
    create_date = models.DateTimeField
    update_user = models.CharField(max_length=50)
    update_date = models.DateTimeField
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    thumb_image_url = models.CharField(max_length=1000)
    full_image_url = models.CharField(max_length=1000)
    detail_url = models.CharField(max_length=1000)
    sum_votes = models.IntegerField(default=0)
