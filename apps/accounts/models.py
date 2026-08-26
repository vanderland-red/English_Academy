from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager


# AbstractBaseUser >> امکانات اصلی حساب کاربری مثل پسورد و ورود
# PermissionsMixin >> مجوزها، گروه‌ها و سطح دسترسی

class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=150, unique=True)
    phone = models.CharField(max_length=11, unique=True)
    email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    is_staff = models.BooleanField(default=False) # برای ورود کاربر ادمین


    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username', 'email']

    def __str__(self):
        return self.email or self.phone

	
    class Meta:
        db_table = 'users'