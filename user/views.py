from django.shortcuts import redirect, render
from django.contrib.auth import login,authenticate,logout
from .models import Profile

# Create your views here.
def user_login(request):
    username,password,message='','',''
    if request.method=='POST':
        username= request.POST['username'] 
        password= request.POST['password'] 

        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user) # request.user
            return redirect('cases')

        #帳號錯誤
        if Profile.objects.filter(username=username).exists():
            message='密碼錯誤'
        else:
            message='帳號錯誤'

        print('登入失敗')


    return render(request,'./user/login.html',{'username':username,'password':password,'message':message})

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('cases')