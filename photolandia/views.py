from django.urls import reverse_lazy
from django.views import generic

class IndexView(generic.RedirectView):
    url = '/photos/'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
