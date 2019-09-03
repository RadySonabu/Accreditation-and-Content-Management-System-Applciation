from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
import datetime
from PIL import Image
from choices.models import Role, College, Program


class MyUserManager(BaseUserManager):
    def create_user(self,

                    first_name, middle_initial, last_name,
                    college,
                    email,
                    contact,
                    role,
                    program,
                    password=None):
        """
        Creates and saves a User with the given email, favorite color
         and password.
        """
        if not email:
            raise ValueError('Users must have a institutional email address')

        user = self.model(

            first_name=first_name,
            middle_initial=middle_initial,
            last_name=last_name,
            email=self.normalize_email(email),
            contact=contact,
            role=role,
            college=college,
            program=program,

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, middle_initial,
                         college,
                         last_name,
                         role,
                         program,
                         contact,
                         email,
                         password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email=email,
            first_name=first_name,
            middle_initial=middle_initial,
            last_name=last_name,
            role=role,
            contact=contact,

            password=password,
            college=college,
            program=program,



        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):

    email = models.EmailField(primary_key=True,  max_length=254)
    first_name = models.CharField(max_length=50)
    middle_initial = models.CharField(max_length=1)
    last_name = models.CharField(max_length=50)

    contact = models.CharField(validators=[
        RegexValidator(r'^(09|\+639)\d{9}$')], blank=True, max_length=13)
    role = models.ForeignKey(
        Role, on_delete=models.SET_NULL, null=True, blank=True)
    college = models.ForeignKey(
        College, on_delete=models.SET_NULL, null=True, blank=True)
    program = models.ForeignKey(
        Program, on_delete=models.SET_NULL, null=True, blank=True)
    date_added = models.DateTimeField(null=True, auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'middle_initial',
                       'last_name', 'role', 'college', 'program',  'contact',

                       ]

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.role}'

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Profile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user} - Profile'

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 200 or img.width > 200:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.image.path)
