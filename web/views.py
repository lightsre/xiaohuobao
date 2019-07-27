from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def web_home(request):
    return render_to_response('web/login.html')

def web_info(request):
    return render(request, 'web/info.html')

def web_name_input(request):
    return render(request, 'web/name_input.html')

def web_name_see(request):
    return render(request, 'web/name_see.html')


def web_in_input(request):
    return render(request, 'web/info.html')


def web_in_see(request):
    return render(request, 'web/info.html')


def web_out_input(request):
    return render(request, 'web/info.html')


def web_out_see(request):
    return render(request, 'web/info.html')


def web_profit_see(request):
    return render(request, 'web/info.html')



@csrf_exempt
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                response = HttpResponseRedirect('web/webinfo')
                response.set_cookie('username',username,86400)
                return response
            else:
                return  HttpResponse('Please check the user and password, login again!')
        else:
            return  HttpResponse('With the registered password is not correct!')
    else:
        return render_to_response('web/login.html')

