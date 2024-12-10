from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('change_passwordadmin/', views.change_passwordadmin, name='change_passwordadmin'),



    path('user_login/', views.user_login, name='user_login'),
    path('user_signup/', views.user_signup, name='user_signup'),
    path('user_home/', views.user_home, name='user_home'),
    path('change_passworduser/', views.change_passworduser, name='change_passworduser'),
    path('view_user/', views.view_user, name='view_user'),


    path('recruiter_login/', views.recruiter_login, name='recruiter_login'),
    path('recruiter_signup/', views.recruiter_signup, name='recruiter_signup'),
    path('recruiter_home/', views.recruiter_home, name='recruiter_home'),
    path('change_passwordrecruiter/', views.change_passwordrecruiter, name='change_passwordrecruiter'),
    path('recruiter_pending/', views.recruiter_pending, name='recruiter_pending'),
    path('recruiter_accepted/', views.recruiter_accepted, name='recruiter_accepted'),
    path('recruiter_rejected/', views.recruiter_rejected, name='recruiter_rejected'),
    path('recruiter_all/', views.recruiter_all, name='recruiter_all'),
    path('delete_recruiter/<int:pid>', views.delete_recruiter, name='delete_recruiter'),
    path('delete_user/<int:pid>', views.delete_user, name='delete_user'),
    path('add_job/', views.add_job, name='add_job'),
    path('job_list/', views.job_list, name='job_list'),




    path('change_status/<int:pid>', views.change_status, name='change_status'),
    path('user_logout/', views.user_logout, name='user_logout'),
]