from django.shortcuts import render, render_to_response, loader
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext,Context
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from web.models import Goods_name, Goods_in, Goods_out, Goods_profit

# Create your views here.
def web_home(request):
    return render_to_response('web/login.html')

def web_info(request):
    return render(request, 'web/info.html')

@csrf_exempt
def web_name_see(request):
    if request.method == "POST":
        goods_name_html = request.POST.get('web_name_html','')
        goods_model_html = request.POST.get('web_model_html','')
        goods_firm_html = request.POST.get('web_firm_html','')
        goods_add_html = request.POST.get('web_add_html','')
        goods_select_html = request.POST.get('web_select_html','')
        if goods_add_html == "新增":
            try:
                db_result = Goods_name.objects.create(name_name=goods_name_html, name_model=goods_model_html, name_firm=goods_firm_html)
            except:
                db_result = 1
            name_info = Goods_name.objects.all()
        elif goods_select_html == "查询":
            goods_condition = {}
            if goods_name_html != "":
                goods_condition["name_name__contains"] = goods_name_html
            if goods_model_html != "":
                goods_condition["name_model__contains"] = goods_model_html
            if goods_firm_html != "":
                goods_condition["name_firm__contains"] = goods_firm_html
            if not goods_condition :
                name_info = Goods_name.objects.all()
            else:
                name_info = Goods_name.objects.filter(**goods_condition)
    else:
        name_info = Goods_name.objects.all()
    context = {'name_info': name_info}
    return render(request,'web/name_see.html',context)

@csrf_exempt
def web_in_see(request):
    if request.method == "POST":
        goods_price_html = request.POST.get('web_price_html','')
        goods_number_html = request.POST.get('web_number_html','')
        goods_starttime_html = request.POST.get('web_starttime_html','')
        goods_endtime_html = request.POST.get('web_endtime_html','')
        goods_nameid_html = request.POST.get('web_nameid_html','')
        goods_add_html = request.POST.get('web_add_html','')
        goods_select_html = request.POST.get('web_select_html','')
        if goods_add_html == "新增":
            try:
                db_result = Goods_in.objects.create(name_id=goods_nameid_html, in_price=goods_price_html, in_number=goods_number_html)
            except:
                db_result = 1
            in_info = Goods_in.objects.all()
        elif goods_select_html == "查询":
            goods_condition = []
            if goods_price_html != "":
                goods_condition.append('a.in_price=%s' % goods_price_html)
            if goods_number_html != "":
                goods_condition.append('a.in_number=%s' % goods_number_html)
            goods_condition = ' or '.join(goods_condition)
            if not goods_condition :
		in_info = Goods_in.objects.raw('''SELECT a.in_id, a.in_price, a.in_number, a.in_time, b.name_name, b.name_model, b.name_firm FROM abcd_Goods_in a LEFT JOIN abcd_Goods_name b ON a.name_id_id = b.name_id ''')
            else:
                in_info = Goods_in.objects.raw('''SELECT a.in_id, a.in_price, a.in_number, a.in_time, b.name_name, b.name_model, b.name_firm FROM abcd_Goods_in a LEFT JOIN abcd_Goods_name b ON a.name_id_id = b.name_id WHERE ( %s ) ''' % goods_condition)
    else:
        in_info = Goods_in.objects.raw('''SELECT a.in_id, a.in_price, a.in_number, a.in_time, b.name_name, b.name_model, b.name_firm FROM abcd_Goods_in a LEFT JOIN abcd_Goods_name b ON a.name_id_id = b.name_id ''')
        
    context = {'in_info': in_info}
    return render(request,'web/name_see.html',context)

@csrf_exempt
def web_out_see(request):
    return render(request, 'web/info.html')

@csrf_exempt
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

