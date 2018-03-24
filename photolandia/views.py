from django.urls import reverse, reverse_lazy
from django.views import generic
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login                    
import json


class IndexView(generic.RedirectView):
    url = '/photos/'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


@csrf_exempt
def api_login(request):
        print('request.POST:', request.POST)
        if request.method == 'POST':
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            print('user:', user)
            if user:
                return JsonResponse({
		    'message': "Thank you for logging in.",
		    'id': user.id,
		    'username': user.username,
		    'token': user.auth_token.key
		})
            else:
                return JsonResponse({
		    'message': 'Bad username or password.',
                    'id': None,
                    'username': None,
                    'token': None
                })
