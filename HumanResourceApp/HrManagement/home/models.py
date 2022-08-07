from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from datetime import timezone

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifier
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('Users must have an email address'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)



class Specialization(models.Model):
    name=models.CharField(max_length=300,null=True,blank=True)

    def __str__(self):
        return self.name


class Provinces(models.Model):
    name=models.CharField(max_length=300,null=True,blank=True)
    code=models.CharField(max_length=5,null=True,blank=True)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    objects = CustomUserManager()

    first_name=models.CharField(max_length=30,null=True,blank=True)
    username=models.CharField(max_length=30,null=True,blank=True)
    last_name=models.CharField(max_length=30,null=True,blank=True)
    email=models.EmailField(max_length=50,null=True,blank=True,unique=True)
    specialization=models.ForeignKey(Specialization,on_delete=models.CASCADE,null=True,blank=True)
    provinces=models.ForeignKey(Provinces,on_delete=models.CASCADE,null=True,blank=True)
    address=models.CharField(max_length=30,null=True,blank=True)
    updated=models.DateTimeField(auto_now=True, null=True ,blank= True)
    

    resume=models.FileField(null=True,blank=True)


    def __str__(self):
        return self.email
    
    def update(self, *args, **kwargs):
        kwargs.update({'updated': timezone.now})
        super().update(*args, **kwargs)

        return self

 

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return (str(self.first_name) + str(self.last_name))

    def get_short_name(self):
        # The user is identified by their Username address
        return self.first_name    


    def __str__(self):              
        return self.email

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        return True
    
    def has_module_perms(self, app_label):

        return True
    class Meta:
        ordering = ['-updated']


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []








