from django.urls import path, include
from login import urls
from . import views

urlpatterns = [
    path('login/', views.logins, name='login'),
    path('addstudent/', views.addstudent, name='addstudent'),
    # path('student/details/', views.detailsstudent, name="studentdetials"),
    path('students/', views.allstudents, name='allstudents'),
    path('student/delete/', views.delete, name='deletestudent'),
    path('student/update/', views.update, name='updateatudentdetails'),
]
