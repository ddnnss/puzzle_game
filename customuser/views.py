from django.shortcuts import render
from .forms import SignUpForm
from django.http import JsonResponse
import json
from django.contrib.auth import login, logout,authenticate

def register(request):

    request_unicode = request.body.decode('utf-8')
    request_body = json.loads(request_unicode)
    data = request.POST.copy()
    print(request_body)
    form = SignUpForm(request_body)
    print(form.errors)
    if form.is_valid():
        new_user = form.save()

        login(request, new_user)
        return JsonResponse({'status': 'success'}, safe=False)
    else:
        return JsonResponse({'status':'error','errors': form.errors}, safe=False)

