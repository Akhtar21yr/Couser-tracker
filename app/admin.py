# from django.contrib import admin

# # Register your models here.
# from .models import User

# admin.site.register(User)

from django.contrib import admin
from .models import User,Course  # Import your custom user model

admin.site.register(User)  # Register your custom user model
admin.site.register(Course)  # Register your custom user model
