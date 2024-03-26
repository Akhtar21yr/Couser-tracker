from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from .models import Course
from django.contrib.auth import authenticate
from .models import User
from .forms import UserForm
from django.http import HttpResponse
from .models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from django.contrib.auth.forms import UserChangeForm



# def login(request):

def home(request):
    user = request.user
    if not user.is_authenticated:
        return render(request,'app/login.html')
    if not user.is_admin or not user.is_staff:
        return redirect('mycourse')
    courses = Course.objects.all()
    return render(request,'app/dashboard.html',context={'courses':courses})

def login_user(request):
    if request.method =='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(password)
        user = authenticate(email=email,password=password)
        print(user)
        if user is not None :
            login(request,user)
            return redirect('home')

    return render(request,'app/login.html')




def addUserView(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            # Redirect to a success page or do something else
            return redirect('home')  # Assuming you have a URL pattern named 'success'
    else:
        form = UserForm()
    return render(request, 'app/adduser.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('home')

def mycourse(request):
    user = request.user
    print('userid...',user.id)
    courses = Course.objects.filter(user=user.id)
    return render(request,'app/mycourse.html',{'courses':courses})

def update_course(request,id):
    user = request.user
    course = Course.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get('course_name')
        course.course_name = name
        course.save()
        if user.is_staff or user.is_admin :
            return redirect('home')
        return redirect('mycourse')


    return render(request,'app/update_course.html',{'course':course})



def view_student(request):
    if request.method == "POST":
        email = request.POST.get('email')
        users = User.objects.filter(email=email)
        if users:
            return render(request,'app/view_student.html',{'users':users})
        else :
            messages.error(request,f'No Student find with this {email} Email')
            print('--------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>....')
            return render(request,'app/view_student.html',{'users':users})

    users = User.objects.all()
    return render(request,'app/view_student.html',{'users':users})

def delete_course(request,id):
    user =request.user
    if user.is_admin:
        course = Course.objects.filter(id=id).first()
        if course :
            course.delete()
            course.save()
            messages.success(request,'course deleted')
            return redirect('home')
    else :
        return redirect('home')

def update_user(request, id):
    user = User.objects.filter(id=id).first()
    if user:
        if request.method == 'POST':
            # Get the updated data from the POST request
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            dob = request.POST.get('dob')
            city = request.POST.get('city')

            # Update the user object with the new data
            user.name = name
            user.phone = phone
            user.dob = dob
            user.city = city

            # Save the updated user object
            user.save()

            # Redirect to a success page or render a success message
            messages.success(request, 'User updated successfully')
            return redirect('view-student')

        # If it's a GET request, render the update_user.html template with the user object
        return render(request, 'app/update_user.html', {'user': user})

    # If the user doesn't exist, show an error message and redirect
    else:
        messages.error(request, 'User not found')
        return redirect('view-student')


# Add this function to your views.py file

def delete_user(request, id):
    # Check if the user is authenticated and has the necessary permissions to delete a user
    if request.user.is_authenticated and (request.user.is_admin):
        # Retrieve the user object based on the provided id
        user = User.objects.filter(id=id).first()
        if user:
            # Delete the user from the database
            user.delete()
            messages.success(request, 'User deleted successfully')
        else:
            messages.error(request, 'User not found')
    else:
        messages.error(request, 'You do not have permission to delete this user')

    # Redirect the user to the appropriate page after deletion
    return redirect('view-student')



