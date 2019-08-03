## 介绍
专门用来记录商品进货出货的平台
适用于小店铺，小商铺，自营店

### 系统环境

- running install Linux
- pyhton (>=3.7)

### 功能列表
1. 商品信息 --- 负责商品的登记，比如商品名字、型号、厂商
2. 商品进货 --- 负责商品的进货填写，关联商品名字，并进行进货信息填写
3. 商品出货 --- 负责商品的出货填写，关联商品名字，并进行出货信息填写
4. 宝宝账单 --- 负责记录商品的盈利，记录销量和金钱

### Linux & Mac 环境准备
- python ( >= 3.7 )
- pip install -r requirements.txt

### 启动方法
  ```
>\# python manage.py makemigrations
>\# python manage.py migrate
>\# python manage.py createsuperuser
>\# python manage.py runserver 0.0.0.0:8000

  ```

#### 界面预览
#### 界面预览
1. 浏览器打开http://IP:8000/admin  输入刚才创建的账号密码

![](https://raw.githubusercontent.com/lightsre/xiaohuobao/master/screenshots/admin-login.png)

2. 创建普通账号，最好多创建一个admin管理账号，admin用户有特效
![](https://raw.githubusercontent.com/lightsre/xiaohuobao/master/screenshots/create-user.png)

3. 由于后面需要用到first用户名称来识别员工，所以配置first名，别忘了点右下角的保存
![](https://raw.githubusercontent.com/lightsre/xiaohuobao/master/screenshots/user-first-name.png)

4.浏览器打开http://IP:8000 并输入创建的test用户登陆

![](https://raw.githubusercontent.com/lightsre/xiaohuobao/master/screenshots/user-lgoin.png)


### 联系方式
mail: xiaohui920@sina.cn

