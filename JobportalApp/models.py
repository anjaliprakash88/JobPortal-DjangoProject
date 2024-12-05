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


class Company(models.Model):
    ceo_name = models.CharField(max_length=10)
    phone = models.CharField(max_length=10)
    image = models.ImageField(upload_to="")
    type = models.CharField(max_length=15)
    status = models.CharField(max_length=20)
    company_name = models.CharField(max_length=100)
    company_address = models.CharField(max_length=100)

    def __str__(self):
        return self.users.company_name
