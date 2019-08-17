from django.db import models

# Create your models here.
class Goods_name(models.Model):
    name_id = models.AutoField(primary_key=True)
    name_name = models.CharField(max_length=100)
    name_model = models.CharField(max_length=100)
    name_firm = models.CharField(max_length=100)

class Goods_in(models.Model):
    in_id = models.AutoField(primary_key=True)
    name_id = models.IntegerField()
    in_price = models.FloatField()
    in_number = models.IntegerField()
    in_time = models.DateField(auto_now_add=True)

class Goods_out(models.Model):
    out_id = models.AutoField(primary_key=True)
    name_id = models.IntegerField()
    out_price = models.FloatField()
    out_number = models.IntegerField()
    out_time = models.DateField(auto_now_add=True)

class Goods_profit(models.Model):
    profit_id = models.AutoField(primary_key=True)
    name_id = models.IntegerField()
    stock_number = models.IntegerField()
    cost_price = models.FloatField()
    profit_number = models.IntegerField()
    profit_price = models.FloatField()

class User_info(models.Model):
    user_phone = models.CharField(max_length=12) 
    user_name = models.CharField(max_length=100)

class User_Record(models.Model):
    user_name = models.CharField(max_length=100)
    user_phone = models.CharField(max_length=12) 
    car_type = models.CharField(max_length=100)
    car_num = models.CharField(max_length=100)
    repair_project = models.CharField(max_length=300)
    record_remarks = models.CharField(max_length=300)
    record_price = models.FloatField()
    record_time = models.DateField(auto_now_add=True) 