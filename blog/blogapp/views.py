from django.shortcuts import render,redirect,HttpResponse
from blogapp.models import blog
from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.
def home_page(request):
        context={}
        context['data']=blog.objects.filter(is_active=1).order_by('-id')
        # if request.user.id == context['data'].uid:
        #     context['edit']='Can Edit'
        #     return render(request,'blogapp/index.html',context)
        # else:
        return render(request,'blogapp/index.html',context)

    
def add_blog(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            bt=request.POST['title']
            bb=request.POST['content']
            uid=request.user.id
            u=User.objects.get(id=uid)
            b=blog.objects.create(title=bt,blog=bb,uid=u)
            b.save
            return redirect('/user')
        else:
            return render(request,'blogapp/addblog.html')
    else:
        return redirect('/authapp/login')


def edit_blog(request):
    context={}
    if request.user.is_authenticated:
        if request.method=='POST':
            bt=request.POST['title']
            bb=request.POST['content']
            uid=request.user.id
            u=User.objects.get(id=uid)
            b=request.GET['b']
            eb=blog.objects.filter(id=b)
            eb.update(title=bt,blog=bb,uid=u)
            return redirect('/user')
        else:
            b=request.GET['b']
            context['data']=blog.objects.get(id=b)
            return render(request,'blogapp/edit.html',context)
    else:
        return redirect('/authapp/login')
    
def delete_blog(request):
    if request.user.is_authenticated:
        d=request.GET['b']
        bd=blog.objects.filter(id=d)
        bd.update(is_active=0)
        return redirect('/user')
    else:
        return redirect('/authapp/login')
    
def user_info(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            un=request.POST['uname']
            ue=request.POST['uemail']
            ufn=request.POST['ufname']
            uln=request.POST['ulname']
            uu=User.objects.filter(id=request.user.id)
            uu.update(username=un,email=ue,first_name=ufn,last_name=uln)
            return redirect('/user')
        else:
            context={}
            context['data']=blog.objects.filter(Q(is_active=1) & Q(uid=request.user.id)).order_by('-id')
            return render(request,'blogapp/user.html',context)
    else:
        return redirect('/authapp/login')