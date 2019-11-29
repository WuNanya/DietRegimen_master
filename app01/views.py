from django.shortcuts import render,HttpResponse,redirect
from app01 import models
# Create your views here.
def login(request):
    error_msg = ""
    if request.method == "POST":
        try:
            user = request.POST.get("username",None)  #用户输入的用户名
            pwd = request.POST.get("password",None)   #用户输入的密码
            user_obj = models.User.objects.get(user_name = user)
        except Exception as e:
            user_obj = None
        print(user_obj)
        if(user_obj == None):
            error_msg = "用户不存在"
            return render(request, "login.html", {"error_msg": error_msg})
        password = user_obj.password
        if(pwd == password):
            return render(request,"index.html")
        else:
            return render(request,"login.html",{"error_msg":error_msg})
    return render(request,"login.html")
