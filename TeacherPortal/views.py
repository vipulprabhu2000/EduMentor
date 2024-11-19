from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Student

# Create your views here.
def Delete_Student(request,name,subject,marks):
    Student_delete=get_object_or_404(Student,Name__icontains=name,Subject__icontains=subject,Marks__icontains=marks)
    Student_delete.delete()
    Student_list=Student.objects.all()
    return redirect("Home")
    

def Add_Student(request):
    print(request)
    if request.method=="POST":
        Name=request.POST["name"]
        Subject=request.POST["subject"]


        Student_Profile=Student.objects.filter(Name__icontains=Name,Subject__icontains=Subject)

        if Student_Profile:
                Student_Profile.update(Marks=request.POST["marks"])
                messages.success(request,"The Student Already Existed and the record has been updated")
                return redirect("Home") 
        else:
            Student_add=Student.objects.create(Name=Name,Subject=Subject,Marks=request.POST["marks"])
            Student_add.save()
            return redirect("Home")

  
        

def Home(request):
    Student_list=Student.objects.all()
    return render(request,"Home.html",{"Student_list":Student_list})


def login_user(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user =authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            print("Successfull")
            messages.success(request,("You have Succcesfully Logged in"))
            return redirect("Home")
        else:
            messages.success(request,"Login Unsuccessful")
            return redirect("login_user")
    else:
        return render(request,"login.html",{})



def logout_user(request):
    logout(request)
    messages.success(request,("You have been logged out Successfully ....... Thank you for Stopping By..."))
    return redirect("login_user")
