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
    profit_number = models.IntegerField()
    profit_price = models.FloatField()
    all_price = models.FloatField()
