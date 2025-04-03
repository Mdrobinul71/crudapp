from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from account.models import Contact


# Create your views here.
def register(request):
    if request.method=="POST":
        stu_name=request.POST.get('username')
        stu_email=request.POST.get('email')
        stu_password=request.POST.get('password')
        stu_cpassword=request.POST.get('confirm_password')
        #print(stu_name)

        #password match check
        if stu_password !=stu_cpassword:
            messages.error(request,"not match password")
            return redirect('signup')

        #check username alredy have in database
        if User.objects.filter(username=stu_name).exists():
            messages.error(request,"given name and database name match")
            return render(request,'account/register.html')

        # Check if the email already exists in the database
        if User.objects.filter(email=stu_email).exists():
            messages.error(request, "Email already exists.")
            return redirect('signup')

        #if nothing problem create then save database
        user=User.objects.create_user(username=stu_name,email=stu_email,password=stu_password)
        user.save()

        
        login(request,user)
        messages.success(request,"register success")
        return redirect('/')

    return render(request,'account/register.html')

def user_login(request):
    if request.method=="POST":
        stu_name=request.POST.get('username')
        stu_password=request.POST.get('password')
        print(stu_name)

        user=authenticate(request,username=stu_name,password=stu_password)
        if user:
            login(request,user)
            messages.success(request,"login success")
            return redirect('task_list')
        else:
            messages.error(request,"User not login")
            return redirect('sign_up')
    return render(request,'account/login.html')


def user_logout(request):
    logout(request)
    messages.success(request,"logout success")
    return redirect('sign_up')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('messages')

        # Validate input fields
        if not name or not email or not message:
            messages.error(request, "All fields are required.")
            return redirect('contact_page')

        try:
            Contact.objects.create(name=name,email=email,messages=message)
            messages.success(request,"Your message has been sent successfully.")
        except Exception as e:
            messages.error(request,"Something went wrong. Please try again.")
    
    return render(request,'account/contact.html')
