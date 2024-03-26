from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login_user,name='login'),
    path('adduser',views.addUserView,name='adduser'),
    path('logout',views.logout_user,name='logout'),
    path('mycourse',views.mycourse,name='mycourse'),
    path('update_course/<int:id>',views.update_course,name='update-course'),
    path('view',views.view_student,name='view-student'),
    path('update_user/<int:id>',views.update_user,name='update-student'),
    path('delete_course/<int:id>',views.delete_course,name='delete-course'),
    path('delete-user/<int:id>',views.delete_user,name='delete-user')
]