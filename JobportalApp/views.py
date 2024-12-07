from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, "index.html")


def admin_login(request):
    error = ""
    if request.method == 'POST':
        uname = request.POST.get('uname')
        password = request.POST.get('pwd')
        user = authenticate(username=uname, password=password)

        if user is not None:
            if user.is_staff:
                login(request, user)
                error = "No"
            else:
                error = "Yes"
        else:
            error = "Yes"

    d = {'error': error}
    return render(request, "admin_login.html", d)


def user_login(request):
    error = ""
    if request.method == "POST":
        uname = request.POST['uname']
        pwd = request.POST['pwd']
        user = authenticate(username=uname, password=pwd)
        if user:
            try:
                user1 = StudentUser.objects.get(user=user)
                if user1.type == "student":
                    login(request, user)
                    error = "No"
                else:
                    error = "Yes"
            except:
                error = "Yes"
        else:
            error = "Yes"
    d = {'error': error}
    return render(request, "user_login.html", d)


def recruiter_login(request):
    error = ""
    if request.method == "POST":
        uname = request.POST['uname']
        pwd = request.POST['pwd']
        user = authenticate(username=uname, password=pwd)
        if user:
            try:
                user1 = Recruiter.objects.get(user=user)
                if user1.type == "recruiter" and user1.status != 'pending':
                    login(request, user)
                    error = "No"
                else:
                    error = "Yes"
            except:
                error = "Yes"
        else:
            error = "Yes"
    d = {'error': error}
    return render(request, "recruiter_login.html", d)


def recruiter_signup(request):
    error = ""
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        image = request.FILES['image']
        pwd = request.POST['pwd']
        email = request.POST['email']
        contact = request.POST['contact']
        gender = request.POST['gender']
        company = request.POST['company']
        try:
            user = User.objects.create_user(first_name=fname, last_name=lname, username=email, password=pwd)
            Recruiter.objects.create(user=user, mobile=contact, image=image, gender=gender, company=company,
                                     type="recruiter",
                                     status="pending")
            error = "No"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, "recruiter_signup.html", d)


def user_home(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    return render(request, "user_home.html")


def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request, "admin_home.html")


def recruiter_home(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    return render(request, "recruiter_home.html")


def user_signup(request):
    error = ""
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        image = request.FILES['image']
        pwd = request.POST['pwd']
        email = request.POST['email']
        contact = request.POST['contact']
        gender = request.POST['gender']
        try:
            user = User.objects.create_user(first_name=fname, last_name=lname, username=email, password=pwd)
            StudentUser.objects.create(user=user, mobile=contact, image=image, gender=gender, type="student")
            error = "No"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, "user_signup.html", d)


def view_user(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = StudentUser.objects.all()
    d = {'data': data}
    return render(request, "view_users.html", d)


def delete_user(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    student = User.objects.get(id=pid)
    student.delete()
    return redirect('view_user')


def delete_recruiter(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    recruiter = User.objects.get(id=pid)
    recruiter.delete()
    return redirect('recruiter_all')


def recruiter_pending(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Recruiter.objects.filter(status='pending')
    d = {'data': data}
    return render(request, "recruiter_pending.html", d)


def recruiter_accepted(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Recruiter.objects.filter(status='Accept')
    d = {'data': data}
    return render(request, "recruiter_accepted.html", d)


def recruiter_rejected(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Recruiter.objects.filter(status='Reject')
    d = {'data': data}
    return render(request, "recruiter_rejected.html", d)


def recruiter_all(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Recruiter.objects.all()
    d = {'data': data}
    return render(request, "recruiter_all.html", d)


def change_status(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    recruiter = Recruiter.objects.get(id=pid)
    if request.method == "POST":
        s = request.POST['status']
        recruiter.status = s
        try:
            recruiter.save()
            error = "No"
        except:
            error = "Yes"
    d = {'recruiter': recruiter, 'error': error}
    return render(request, "change_status.html", d)


def user_logout(request):
    logout(request)
    return redirect('user_login')
