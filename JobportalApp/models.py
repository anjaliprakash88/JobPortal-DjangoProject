from django.db import models
from django.contrib.auth.models import User


class StudentUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15, null=True)
    image = models.FileField(null=True)
    gender = models.CharField(max_length=10, null=True)
    type = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.user.username


class Recruiter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15, null=True)
    image = models.FileField(null=True)
    gender = models.CharField(max_length=10, null=True)
    company = models.CharField(max_length=10, null=True)
    type = models.CharField(max_length=15, null=True)
    status = models.CharField(max_length=25, null=True)

    def __str__(self):
        return self.user.username


class Job(models.Model):
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    title = models.CharField(max_length=10)
    salary = models.FloatField(max_length=100)
    image = models.FileField(max_length=15)
    description = models.CharField(max_length=300)
    experience = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    skills = models.CharField(max_length=100)
    creationdate = models.DateField()

    def __str__(self):
        return self.title


class Applicant(models.Model):
    applicant_name = models.CharField(max_length=10)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    image = models.ImageField(upload_to="images")
    gender = models.CharField(max_length=10)
    type = models.CharField(max_length=15)
    edu_qualif = models.CharField(max_length=10)
    experience = models.IntegerField()

    def __str__(self):
        return self.users.applicant_name