from django.shortcuts import redirect, render
from django.contrib.auth import login,authenticate,logout


# Create your views here.
def user_login(request):
    if request.method=='POST':
        username= request.POST['username'] 
        password= request.POST['password'] 

        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user) # request.user
            return redirect('cases')

        print('登入失敗')


    return render(request,'./user/login.html')

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('cases')