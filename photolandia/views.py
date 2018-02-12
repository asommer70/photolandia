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
	if request.method == 'POST':
		body_unicode = request.body.decode('utf-8')
		body = json.loads(body_unicode)

		user = authenticate(username=body['username'], password=body['password'])
		if user:
			return JsonResponse({'message': "Thank you for logging in.", 'token': user.auth_token.key})
		else:
			return JsonResponse({'message': 'Bad username or password.'})
	else:
		return HttpResponseRedirect(reverse('photos:list'))