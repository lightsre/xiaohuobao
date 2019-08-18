from django.shortcuts import render, render_to_response, loader
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext,Context
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.db.models import F
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from web.models import Goods_name, Goods_in, Goods_out, Goods_profit, User_record

# Create your views here.
def web_home(request):
    return render_to_response('web/login.html')

def web_info(request):
    return render(request, 'web/info.html')

@csrf_exempt
@login_required
def web_name_see(request):
    if request.method == "POST":
        goods_name_html = request.POST.get('web_name_html','')
        goods_model_html = request.POST.get('web_model_html','')
        goods_firm_html = request.POST.get('web_firm_html','')
        goods_add_html = request.POST.get('web_add_html','')
        goods_select_html = request.POST.get('web_select_html','')

        if goods_add_html == "新增":
            if goods_name_html != "" and goods_model_html !="" and goods_firm_html !="":
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
@login_required
def web_trade_see(request):
    db_command=connection.cursor()
    goods_url_html = request.path
    if goods_url_html == "/web/insee/":
        db_name = "in"
        web_title = "进货账单"
        web_url = goods_url_html
        db_goods = Goods_in
    elif goods_url_html == "/web/outsee/":
        db_name = "out"
        web_title = "出货账单"
        web_url = goods_url_html
        db_goods = Goods_out
    sql_command='SELECT a.%s_id, a.%s_price, a.%s_number, b.name_name, b.name_model, b.name_firm FROM web_goods_%s a LEFT JOIN web_goods_name b ON a.name_id = b.name_id ' % (db_name, db_name, db_name, db_name)
    if request.method == "POST":
        goods_price_html = request.POST.get('web_price_html','')
        goods_number_html = request.POST.get('web_number_html','')
        goods_nameid_html = request.POST.get('web_nameid_html','')
        goods_starttime_html = request.POST.get('web_starttime_html','')
        goods_endtime_html = request.POST.get('web_endtime_html','')
        goods_add_html = request.POST.get('web_add_html','')
        goods_select_html = request.POST.get('web_select_html','')
        if goods_add_html == "新增":
            try:
                db_info = {'name_id': goods_nameid_html, '%s_price' % db_name: goods_price_html, '%s_number' % db_name: goods_number_html }
                #db_result = db_goods.objects.create(name_id=goods_nameid_html, in_price=goods_price_html, in_number=goods_number_html)
                db_result = db_goods.objects.create(**db_info)
                print(db_result)
                print(type(db_result))
            except:
                print('新增失败')
                db_result = 1
            if db_result != 1:
                goods_exist = Goods_profit.objects.filter(name_id=goods_nameid_html)
                if len(goods_exist) == 0:
                    Goods_profit.objects.create(name_id=goods_nameid_html, stock_number=0, cost_price=0, profit_number=0, profit_price=0) 
                goods_info = Goods_profit.objects.filter(name_id=goods_nameid_html)
                if len(goods_info) != 0:               
                    if db_name == "in":                       
                        goods_info.update(stock_number=F('stock_number') + goods_number_html)
                        goods_info.update(cost_price=F('cost_price') + goods_price_html)                   
                    elif db_name == "out":
                        goods_info.update(stock_number=F('stock_number') - goods_number_html)
                        goods_info.update(profit_number=F('profit_number') + goods_number_html)
                        goods_info.update(profit_price=F('profit_price') + goods_price_html)
                
        elif goods_select_html == "查询":
            goods_condition = []
            if goods_price_html != "":
                goods_condition.append('a.%s_price=%s' % (db_name, goods_price_html))
            if goods_number_html != "":
                goods_condition.append('a.%s_number=%s' % (db_name, goods_number_html))
            if goods_nameid_html != "":
                goods_condition.append('b.name_id=%s' % goods_nameid_html)
            goods_condition = ' or '.join(goods_condition)
            if goods_starttime_html != "" and goods_endtime_html != "" and goods_condition != "":
                goods_condition = goods_condition + ' AND in_time between "%s" AND "%s"' % (goods_starttime_html, goods_endtime_html)
            if goods_condition:
                sql_command = sql_command + "WHERE ( %s )" % goods_condition
    name_info = Goods_name.objects.all()
    trade_communt = db_command.execute(sql_command)  
    trade_info = db_command.fetchall()
    context = {'trade_info': trade_info, 'name_info': name_info, 'web_title': web_title, 'web_url': web_url}
    return render(request,'web/trade_see.html',context)

@csrf_exempt
@login_required
def web_profit_see(request):
    db_command=connection.cursor()
    db_name = "profit"
    sql_command='SELECT a.profit_id, a.profit_price, a.profit_number, a.stock_number, a.cost_price, b.name_name, b.name_model, b.name_firm FROM web_goods_profit a LEFT JOIN web_goods_name b ON a.name_id = b.name_id '
    if request.method == "POST":
        goods_nameid_html = request.POST.get('web_nameid_html','')
        goods_condition = []
        if goods_nameid_html != "":
            goods_condition.append('b.name_id=%s' % goods_nameid_html)
        goods_condition = ' or '.join(goods_condition)
        if goods_condition:
            sql_command = sql_command + "WHERE ( %s )" % goods_condition
    name_info = Goods_name.objects.all()
    profit_communt = db_command.execute(sql_command)  
    profit_info = db_command.fetchall()
    context = {'profit_info': profit_info, 'name_info': name_info}
    return render(request,'web/profit_see.html',context)

@csrf_exempt
@login_required
def web_user_record(request):
    if request.method == "POST":
        user_name_html = request.POST.get('user_name_html','')
        user_phone_html = request.POST.get('user_phone_html','')
        car_type_html = request.POST.get('car_type_html','')
        car_num_html = request.POST.get('car_num_html','')
        repair_project_html = request.POST.get('repair_project_html','')
        record_remarks_html = request.POST.get('record_remarks_html','')
        record_price_html = request.POST.get('record_price_html','')
        record_status_html = request.POST.get('record_status_html','')
        record_add_html = request.POST.get('web_add_html','')
        record_select_html = request.POST.get('web_select_html','')

        if record_add_html == "新增":
            if user_name_html != "" and user_phone_html !="" and repair_project_html !="" and record_price_html !="":
                try:
                    db_result = User_record.objects.create(user_name=user_name_html, user_phone=user_phone_html, car_type=car_type_html, car_num=car_num_html, repair_project=repair_project_html, record_remarks=record_remarks_html, record_price=record_price_html)
                except:
                    db_result = 1
            record_info = User_record.objects.all()
        elif record_select_html == "查询":
            record_condition = {}
            if user_name_html != "":
                record_condition["user_name__contains"] = user_name_html
            if user_phone_html != "":
                record_condition["user_phone__contains"] = user_phone_html
            if repair_project_html != "":
                record_condition["repair_project__contains"] = repair_project_html
            if not record_condition :
                record_info = User_record.objects.all()
            else:
                if record_status_html != "":
                    record_info = User_record.objects.filter(**record_condition, record_status=record_status_html)
                else:
                    record_info = User_record.objects.filter(**record_condition)
    else:
        record_info = User_record.objects.all()
    context = {'record_info': record_info}
    return render(request,'web/record_see.html',context)    

@csrf_exempt
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        error_msg = "Please check the user and password !!!"
        if user is not None:
            if user.is_active:
                login(request, user)
                response = HttpResponseRedirect('web/webinfo/')
                response.set_cookie('username',username,86400)
                return response
            else:
                return render(request,'web/login.html',{'error_msg':error_msg})
        else:
            return render(request,'web/login.html',{'error_msg':error_msg})
    else:
        return render_to_response('web/login.html')

def logout_view(request):
    logout(request)
    return render_to_response('web/login.html')
