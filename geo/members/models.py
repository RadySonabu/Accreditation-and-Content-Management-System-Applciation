from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
import datetime


class MyUserManager(BaseUserManager):
    def create_user(self, employee_number, first_name, middle_initial, last_name, college, program, email, contact, course, password=None):
        """
        Creates and saves a User with the given email, favorite color
         and password.
        """
        if not employee_number:
            raise ValueError('Users must have a employee number')

        user = self.model(
            employee_number=employee_number,
            first_name=first_name,
            middle_initial=middle_initial,
            last_name=last_name,
            email=self.normalize_email(email),
            contact=contact,
            course=course,
            college=college,
            program=program,

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, employee_number, first_name, middle_initial, college, program, last_name, course, contact, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            employee_number,
            first_name=first_name,
            middle_initial=middle_initial,
            last_name=last_name,
            course=course,
            contact=contact,
            email=email,
            password=password,
            college=college,
            program=program,


        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    ROLE_CHOICES = (
        ('VPAA', 'Vice President for Academic Affairs'),
        ('Dean', 'Dean of College'),
        ('DC', 'Department Chairperson'),
        ('AD ', 'Administration')
    )
    COLLEGE_CHOICES = (
        ('CITE', 'College of Information Technology Education'),
        ('CEA', 'College of Engineering and Architecture'),
        ('CBE', 'College of Business Eduction'),
        ('COA', 'College of Arts'),
        ('N/A', 'Not Applicable')
    )
    PROGRAM_CHOICES = (
        ('BSCS', 'Bachelor of Science in Computer Science'),
        ('BSIT', 'Bachelor of Science in Information Technology'),
        ('BSIS', 'Bachelor of Science in Information Systems'),
        ('BSEMC', 'Bachelor of Science in Entertainment Multimedia Education'),
        ('BSCE', 'Bachelor of Science in Civil Engineering'),
        ('BSIE', 'Bachelor of Science in Industrial Engineering'),
        ('N/A', 'Not Applicable'),
    )

    employee_number = models.CharField(primary_key=True, max_length=7, validators=[
        RegexValidator(r'^\d{1,10}$')])

    first_name = models.CharField(max_length=50)
    middle_initial = models.CharField(max_length=1)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(blank=True, max_length=254)
    contact = models.CharField(validators=[
    RegexValidator(r'^(09|\+639)\d{9}$')], blank=True, max_length=13)
    course = models.CharField(choices=ROLE_CHOICES, max_length=50)
    college = models.CharField(choices=COLLEGE_CHOICES, max_length=50, null=True)
    program = models.CharField(choices=PROGRAM_CHOICES, max_length=50, null=True)
    date_added = models.DateTimeField(null=True, auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'employee_number'
    REQUIRED_FIELDS = ['first_name', 'middle_initial',
                       'last_name', 'course', 'college', 'program', 'contact', 'email']

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return f'{self.employee_number} - {self.first_name} {self.last_name} {self.course}'

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
