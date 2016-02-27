from django.db import connection
from django.shortcuts import redirect
from django.views.generic import ListView
from django.shortcuts import render_to_response

from BestPicturePolls.models import BestPictureNominee


class PollsView(ListView):
    model = BestPictureNominee
    template_name = "polls.html"
    context_object_name = "best_picture_nominee_list"

    def get_queryset(self):
        return BestPictureNominee.objects.raw('SELECT * FROM t_best_picture_nominee')


class ResultsView(ListView):
    model = BestPictureNominee
    template_name = "results.html"
    context_object_name = "best_picture_nominee_list"

    def get_queryset(self):
        return BestPictureNominee.objects.raw('SELECT * FROM t_best_picture_nominee')


def ChartsView(request):
    nominees = BestPictureNominee.objects.raw('SELECT * FROM t_best_picture_nominee')
    xdata = []
    ydata = []
    for nominee in nominees:
        xdata.append(nominee.name)
        ydata.append(nominee.sum_votes)
    extra = {
        "tooltip": {"y_start": "", "y_end": " votes"}
    }
    chartdata = {'x': xdata, 'y': ydata, 'extra': extra}
    charttype = "pieChart"
    data = {
        'charttype': charttype,
        'chartdata': chartdata
    }
    return render_to_response('charts.html', data)


def VoteForBestPicture(request, best_picture_nominee_id):
    cursor = connection.cursor()
    cursor.execute("UPDATE t_best_picture_nominee SET sum_votes = sum_votes + 1 WHERE best_picture_nominee_id = %s",
                   [best_picture_nominee_id])
    return redirect('results')
