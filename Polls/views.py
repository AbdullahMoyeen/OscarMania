from django.http import HttpResponse
from django.views import generic
from Polls.models import BestPictureNominee


# def home(request):
#     return HttpResponse("Hello, world!")


class HomeView(generic.ListView):
    template_name = "home.html"
    context_object_name = "best_picture_nominee_list"

    def get_queryset(self):

        return BestPictureNominee.objects.raw('SELECT * FROM t_best_picture_nominee')
