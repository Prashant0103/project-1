from django.shortcuts import redirect, render
from .forms import uform,postform
from django.contrib import auth,messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView




@login_required(login_url='/')
def logoutt(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/')
def textpo(request):
    return render(request,'index.html')

@login_required(login_url='/')
def next(request):
    return render(request,'index.html')


def loginn(request):
    return render(request,'login.html')

@login_required(login_url='/')
def verifyu(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        passw = request.POST.get('password')
        
        user = authenticate(username=uname,password=passw)
        if user:
            login(request,user)
            messages.success(request,'Your Login Successfully')
            return redirect('/one')
        else:
            messages.error(request,'plz enter valid username and password')
            return render(request,'login.html')
    else:
        messages.error(request,'error')
        return render(request,'login.html')

@login_required(login_url='/')
def userf(request):
    if request.method=="POST":
            form = uform()
            form = uform(request.POST)
            if form.is_valid():
                user = form.save()
                user.save()
                profile = form.save(commit=False)
                profile.user = user            
                profile.save()
                registered = True
                messages.success(request,'Your Reg Successfully')
                return redirect('/one')
            else:
                return redirect('/')
        
    else:
        form = uform()
        return render(request,'one.html',{'form':form})
     
@login_required(login_url='/')   
def postt(request):
    if request.method=="POST":
            form = postform()
            form = postform(request.POST)
            if form.is_valid():
                print('hii')
                user = form.save()
                user.save()
                profile = form.save(commit=False)
                profile.user = user            
                profile.save()
                registered = True
                messages.success(request,'Your Reg Successfully')
                return redirect('/one')
            else:
                return redirect('/one')
        
    else:
        form = postform()
        return render(request,'index.html',{'form':form})
    