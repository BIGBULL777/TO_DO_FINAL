from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
import json 
#added extra for API
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from tasks.models import *
from todo.serializers import Time_createdSerializers,TaskSerializers
from django.shortcuts import get_object_or_404

# def LoginUser(request):
#     if request.method == "POST":
#         UserName = request.POST['UserName']
#         password = request.POST['password']
#         User = authenticate(UserName = UserName,password = password)
#         # print(UserName,password)
#         if User is not None:
#             login(request, User)
#             return redirect('/navbar')
#         else:
#             return render(request, 'login.html')
#     return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return render(request, 'logout.html')


def tasks(request):
    # if request.user.is_anonymous:
    #     return redirect('/login')
    # else:

        all_time = time.objects.all()
        datas = {}
        for i in range(all_time.count()):
            title = task.objects.filter(time_created = all_time[i])
            datas[f'{all_time[i].title}'] = title
        
    
        form =  taskform()
        if request.method == 'POST':

            form = taskform(request.POST)
            if form.is_valid():
                form.save()
            return redirect('/')
        context = { 'form': form,'mydict': datas}
        return render(request,'landing.html',context)



def newtable(request):
    form1 = Timeform()
    if request.method == 'POST':
        form1 = Timeform(request.POST)
        if form1.is_valid():
            form1.save()
        return redirect('home')
    context = {'form1':form1}
    return render(request,'table.html')


def times(request):
    all_time = time.objects.all()
    context = {'time':all_time}
    return render(request,'home.html',context)

def newform(request):
    form1 = Timeform()
    if request.method == 'POST':
        form1 = Timeform(request.POST)
        if form1.is_valid():
            form1.save()
        return redirect('home')
    context = { 'form1': form1 }
    return render(request,'table.html',context)


def handleSignup(request):
        if request.method == 'POST':
            username = request.POST['username']
            First_Name = request.POST['First_Name']
            Last_Name = request.POST['Last_Name']
            password = request.POST['Password']
            confirm = request.POST['Passcode']
            print(username)
    #create user
            myuser = User.objects.create_user(username = username,first_name = First_Name,last_name = Last_Name,password = password )
            myuser.first_name = First_Name
            myuser.lastname = Last_Name
            myuser.save()
            messages.success(request,'Your account has been created')
            return redirect('login')
        return render(request, 'signup.html')
        
class Taskapi(APIView):
    def get(self,request):
        task1 = task.objects.all()
        serializer = TaskSerializers(task1,many = True)
        return Response(serializer.data)
    def post(self):
        pass

class Time_createdAPI(APIView):
    def get(self,request):
        task2 = time.objects.all()
        serializer1 = Time_createdSerializers(task2,many = True)
        return Response(serializer1.data)
    def post(self):
        pass

def Update_task(request,pk):
    Task = task.objects.get(id = pk)
    form = taskform(instance=Task or request.POST)
    if form.is_valid():
            form.save()
            return redirect('home')
    # print(form)
    context = {'form':form}
    return render(request,'update_task.html',context)


def Updatetable(request,pk):
    times = time.objects.get(id = pk)
    form = Timeform(instance=times)
    if request.method == 'POST':
        form2 = form(request.POST) 
        if form.is_valid():
            form.save()
        return redirect('/home')
        
    context = {'form':form}
    return render(request,'updateTable.html',context)





def loginUser(request):
    if request.method == "POST":
        username=request.POST.get('username',False)
        password=request.POST.get('password',False)
        user = authenticate(username=username, password=password)
        # print(username,password)
        if user is not None:
            login(request,user)
            return redirect("/home")
        else:
            return render(request,'login.html')
    return render(request,'login.html')




def Delete_task(request,pk):
    Delete_entry = task.objects.get(id= pk)
    if request.method == 'POST':
        Delete_entry.delete()
        return redirect('/home')
    context = {'Delete_entry':Delete_entry}
    return render(request,'delete.html',)
