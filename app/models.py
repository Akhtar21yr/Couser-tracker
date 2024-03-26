# app/models.py

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.core.validators import EmailValidator, MinLengthValidator, RegexValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, email, name, phone, password=None, **extra_details):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, phone=phone, **extra_details)
        print('-0................dddddddd.d................s...............s')
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, phone, password=None, **extra_details):
        extra_details.setdefault('is_staff', True)
        extra_details.setdefault('is_admin', True)
        # if password:
        #     password = make_password(password)
        return self.create_user(email, name, phone, password, **extra_details)

def name_validator(name):
    name = name.split()
    for i in name :
        if not i.isalpha():
            raise ValidationError('Name should be alphabetic')

class User(AbstractBaseUser):
    email = models.EmailField(unique=True, validators=[EmailValidator(message='Please enter a correct email')])
    name = models.CharField(max_length=100, validators=[MinLengthValidator(5, message='Name should be at least 5 characters'), name_validator])
    phone = models.CharField(max_length=10, validators=[RegexValidator(regex=r'^[0-9]{10}$', message='Number should be 10 digits')], unique=True)
    dob = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    CHOICE = [
        ('superuser','SuperUser'),
        ('student','Student')
    ]
    user_type = models.CharField(max_length = 20,choices=CHOICE)


    USERNAME_FIELD = 'email'  # Field to use for login
    REQUIRED_FIELDS = ['name', 'phone', 'is_admin']

    objects = UserManager()

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    # @property
    # def is_staff(self):
    #     "Is the user a member of staff?"
    #     # Simplest possible answer: All admins are staff
    #     return self.is_admin

class Course(models.Model):
    user = models.ForeignKey('User',on_delete=models.CASCADE)
    course_name = models.CharField(max_length = 220)
    create_at = models.DateTimeField(auto_now_add = True) #automoticat add when created
    updated_at = models.DateTimeField(auto_now = True) # automatic updtaed when we update 
    is_active = models.BooleanField(default = True)

