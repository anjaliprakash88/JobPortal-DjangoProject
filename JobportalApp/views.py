from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import date


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
    user = request.user
    student = StudentUser.objects.get(user=user)
    error = ""
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        contact = request.POST['contact']
        gender = request.POST['gender']

        student.user.first_name = fname
        student.user.last_name = lname
        student.mobile = contact
        student.gender = gender
        student.user.username = email
        try:
            student.save()
            student.user.save()
            error = "No"
        except:
            error = "yes"

        try:
            img = request.FILES['image']
            student.image = img
            student.save()
            error = "No"
        except:
            pass

    context = {'student': student, 'error': error}
    return render(request, "user_home.html", context)


def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request, "admin_home.html")


def recruiter_home(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    user = request.user
    recruiter = Recruiter.objects.get(user=user)
    error = ""
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        contact = request.POST['contact']
        gender = request.POST['gender']

        recruiter.user.first_name = fname
        recruiter.user.last_name = lname
        recruiter.mobile = contact
        recruiter.gender = gender
        recruiter.user.username = email
        try:
            recruiter.save()
            recruiter.user.save()
            error = "No"
        except:
            error = "yes"

        try:
            img = request.FILES['image']
            recruiter.image = img
            recruiter.save()
            error = "No"
        except:
            pass

    context = {'recruiter': recruiter, 'error': error}
    return render(request, "recruiter_home.html", context)


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


def change_passwordadmin(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    if request.method == "POST":
        current = request.POST['currentpassword']
        new = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(current):
                u.set_password(new)
                u.save()
                error = "No"
            else:
                error = "not"
        except:
            error = "Yes"
    d = {'error': error}
    return render(request, "change_passwordadmin.html", d)


def change_passworduser(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    error = ""
    if request.method == "POST":
        current = request.POST['currentpassword']
        new = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(current):
                u.set_password(new)
                u.save()
                error = "No"
            else:
                error = "not"
        except:
            error = "Yes"
    d = {'error': error}
    return render(request, "change_passworduser.html", d)


def change_passwordrecruiter(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    error = ""
    if request.method == "POST":
        current = request.POST['currentpassword']
        new = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(current):
                u.set_password(new)
                u.save()
                error = "No"
            else:
                error = "not"
        except:
            error = "Yes"
    d = {'error': error}
    return render(request, "change_passwordrecruiter.html", d)


def add_job(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    error = ""
    if request.method == 'POST':
        jtitle = request.POST['jobtitle']
        sdate = request.POST['startdate']
        edate = request.POST['enddate']
        salary = request.POST['salary']
        logo = request.FILES['logo']
        experience = request.POST['experience']
        location = request.POST['location']
        skills = request.POST['skills']
        desc = request.POST['description']
        user = request.user
        recruiter = Recruiter.objects.get(user=user)
        try:
            Job.objects.create(recruiter=recruiter, start_date=sdate, end_date=edate, title=jtitle,
                               salary=salary, image=logo, description=desc, experience=experience,
                               location=location, skills=skills, creationdate=date.today())
            error = "No"
        except:
            error = "yes"
    d = {'error': error}

    return render(request, "add_job.html", {'d': d})


def job_list(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    user = request.user
    recruiter = Recruiter.objects.get(user=user)
    data = Job.objects.filter(recruiter=recruiter)
    d = {'data': data}
    return render(request, "job_list.html", d)


def edit_jobdetails(request, pid):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    error = ""
    job = Job.objects.get(id=pid)
    if request.method == 'POST':
        jtitle = request.POST['jobtitle']
        sdate = request.POST['startdate']
        edate = request.POST['enddate']
        salary = request.POST['salary']
        experience = request.POST['experience']
        location = request.POST['location']
        skills = request.POST['skills']
        desc = request.POST['description']
        user = request.user
        recruiter = Recruiter.objects.get(user=user)

        job.title = jtitle
        job.salary = salary
        job.experience = experience
        job.location = location
        job.skills = skills
        job.description = desc
        try:
            job.save()
            error = "No"
        except:
            error = "Yes"
        if sdate:
            try:
                job.start_date = sdate
                job.save()
            except:
                pass
        if edate:
            try:
                job.end_date = edate
                job.save()
            except:
                pass

    context = {'error': error, 'job': job}
    return render(request, "edit_jobdetails.html", context)


def change_companylogo(request, pid):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    error = ""
    job = Job.objects.get(id=pid)
    if request.method == 'POST':
        change_image = request.FILES['logo']

        job.image = change_image
        try:
            job.save()
            error = "No"
        except:
            error = "Yes"
    context = {'error': error, 'job': job}
    return render(request, "change_companylogo.html", context)


def latest_jobs(request):
    data = Job.objects.all().order_by('-start_date')
    d = {'data': data}
    return render(request, "latest_jobs.html", d)


def user_latestjobs(request):
    data = Job.objects.all().order_by('-start_date')
    d = {'data': data}
    return render(request, "user_latestjobs.html", d)


def user_logout(request):
    logout(request)
    return redirect('user_login')
