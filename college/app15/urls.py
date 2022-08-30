from django.urls import path
from app15 import views
urlpatterns=[
    path('',views.index,name='index'),
    path('main',views.main,name='main'),
    path('login',views.login,name='login'),
    path('studreg',views.stud,name='studreg'),
    path('empreg',views.emp,name='empreg'),
    path('student',views.student,name='student'),
    path('attendence',views.attendence,name='attendence'),
    path('studperform',views.studperform,name='studperform'),
    path('employee',views.employee,name='employee'),
    path('employeeattend',views.employeeattend,name='employeeattend'),
    path('viewstud',views.viewstud,name='viewstud'),
    path('viewemp',views.viewemp,name='viewemp'),
    # path('stud',views.stud,name='stud'),
    path('emp',views.emp,name='emp'),
    path('adminpage', views.admin, name='adminpage'),
    path('customer', views.customer, name='customer'),
    
    path('empe', views.empe, name='empe'),
    path('login_view',views.login_view,name='login_view'),
    path('register',views.register,name='register'),
]
    
