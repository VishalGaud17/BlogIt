from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User

# Create your views here.
def user_login(request):
    if request.method=='POST':
        context={}
        un=request.POST['uname']
        up=request.POST['upass']
        if un=='' or up=='':
            context['errmsg']='Fields cannot be Empty'
            return render(request,'authapp/login.html',context)
        else:
            user=authenticate(username=un,password=up)
            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                context['errmsg']="Invalid Username and Password"
                return render(request,'authapp/login.html',context)
    else:
        return render(request,'authapp/login.html')
    

def user_register(request):
    context={}
    if request.method=='POST':
        try:
            un=request.POST['uname']
            up=request.POST['upass']
            ucp=request.POST['ucpass']
            ue=request.POST['uemail']
            if un=='' or up=='' or ucp=='' or ue=='':
                context['errmsg']='Fields cannot be Empty'
                return render(request,'authapp/register.html',context)
            elif up!=ucp:
                context['errmsg']="Password and Confirm Password didn't Match"
                return render(request,'authapp/register.html',context)
            else:
                u=User.objects.create(username=un,email=ue)
                u.set_password(up)
                u.save()
                context['success']="User Created Successfully, please Login"
                return render(request,'authapp/register.html',context)
        except Exception:
            context['errmsg']='User Already Exists'
            return render(request,'authapp/register.html',context)
    else:
        return render(request,'authapp/register.html')
    
def user_logout(request):
    logout(request)
    return redirect('/authapp/login')
