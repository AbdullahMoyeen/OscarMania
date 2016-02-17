from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.views import generic
from Polls.models import BestPictureNominee


class HomeView(generic.ListView):
    template_name = "home.html"
    context_object_name = "best_picture_nominee_list"

    def get_queryset(self):
        return BestPictureNominee.objects.raw('SELECT * FROM t_best_picture_nominee')


def VoteForBestPicture(request, best_picture_nominee_id):
    return redirect('home')

# BestPictureNominee.objects.raw(
#     'UPDATE t_best_picture_nominee SET sum_votes = sum_votes + 1 WHERE best_picture_nominee_id = ?',
#     using=best_picture_nominee_id)
