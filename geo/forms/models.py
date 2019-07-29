from django.db import models
from members.models import MyUser

class CoE_IT_FORM(models.Model):

    institution = models.CharField(max_length=100, default='TIP')
    branch = models.CharField(max_length=100, default='MANILA')
    department = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    dean = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    program_chair = models.CharField(max_length=100)


    faculty = models.IntegerField()
    laboratory = models.IntegerField( )
    libraries = models.IntegerField( )
    curriculum = models.IntegerField( )
    program_admin = models.IntegerField( )
    student_report = models.IntegerField( )
    it_capability = models.IntegerField( )
    graduate_programs = models.IntegerField( )
    graduate_profile = models.IntegerField( )
    graduate_tracker = models.IntegerField( )




    def __str__(self):
        return f'{self.dean}'



