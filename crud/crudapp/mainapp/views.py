from django.shortcuts import redirect, render,HttpResponseRedirect
from .forms import Register
from .models import User
# Create your views here.
def home(request):
    if request.method=='POST':
        form=Register(request.POST)
        form.save()
        form=Register()

    else:
        form=Register()
    user=User.objects.all()
    
    return render(request,'mainapp/user.html',{'form':form,'user':user})
    
def update(request,id):
    if request.method=='POST':
        user=User.objects.get(pk=id)
        form=Register(request.POST,instance=user)
        form.save()  
    
    else:
        
        user=User.objects.get(pk=id)
        form=Register(instance=user)
    return render(request,'mainapp/update.html',{'form':form})


def delete(request,id):
    if request.method=='POST':
        
        user=User.objects.get(pk=id)
        user.delete() 
    return HttpResponseRedirect('/')
