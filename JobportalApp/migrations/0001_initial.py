# Generated by Django 5.0.3 on 2024-04-02 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant_name', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('image', models.ImageField(upload_to='images')),
                ('gender', models.CharField(max_length=10)),
                ('type', models.CharField(max_length=15)),
                ('edu_qualif', models.CharField(max_length=10)),
                ('experience', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ceo_name', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=10)),
                ('image', models.ImageField(upload_to='')),
                ('type', models.CharField(max_length=15)),
                ('status', models.CharField(max_length=20)),
                ('company_name', models.CharField(max_length=100)),
                ('company_address', models.CharField(max_length=100)),
            ],
        ),
    ]
