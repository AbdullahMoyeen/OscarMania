from django.db import connection
from django.shortcuts import redirect
from django.views.generic import ListView

from Polls.models import BestPictureNominee


class HomeView(ListView):
    model = BestPictureNominee
    template_name = "home.html"
    context_object_name = "best_picture_nominee_list"

    def get_queryset(self):
        return BestPictureNominee.objects.raw('SELECT * FROM t_best_picture_nominee')


class ResultsView(ListView):
    model = BestPictureNominee
    template_name = "results.html"
    context_object_name = "best_picture_nominee_list"

    def get_queryset(self):
        return BestPictureNominee.objects.raw('SELECT * FROM t_best_picture_nominee')


def VoteForBestPicture(request, best_picture_nominee_id):
    cursor = connection.cursor()
    cursor.execute("UPDATE t_best_picture_nominee SET sum_votes = sum_votes + 1 WHERE best_picture_nominee_id = %s",
                   [best_picture_nominee_id])
    return redirect('results')
