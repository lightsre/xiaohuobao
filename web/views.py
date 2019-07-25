from django.shortcuts import render

# Create your views here.
def web_login(request):
    return render_to_response('web/login.html')

def web_info(request):
    return render(request, 'web/info.html')
