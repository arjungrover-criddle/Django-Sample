from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.conf import settings

from phone_field import PhoneField

class UserManager(BaseUserManager):
    """
    This is my custom user manager
    """
    def _create_user(self, phone_number, password, **extra_fields):
        """
        It will create user with entered phone_number and password
        """
        if not phone_number:
            raise ValueError("The given Phone number must be set")
       
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_user(self, phone_number, password, **extra_fields):
        extra_fields['is_superuser'] = False
        extra_fields['is_staff'] = True
        return self._create_user(phone_number, password, **extra_fields)

    def create_superuser(self, phone_number, password, **extra_fields):
        extra_fields['is_superuser'] = True
        extra_fields['is_staff'] = True
        return self._create_user(phone_number, password, **extra_fields)

# Create your models here.
class UserInfo(AbstractBaseUser, PermissionsMixin):
    phone_number = PhoneField(primary_key=True, help_text='Contact phone number')
    first_name = models.CharField(max_length=255, blank = True )
    last_name = models.CharField(max_length=255, blank = True )
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False, help_text="Designates whether the user can log into this admin site.")
    
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS   = []

    objects = UserManager()

    def __str__(self):
        return "{}:{}".format(self.first_name,self.phone_number)
