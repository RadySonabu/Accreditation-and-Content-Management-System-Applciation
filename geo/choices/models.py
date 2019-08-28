from django.db import models

# Create your models here.


class Role(models.Model):
    role = models.CharField(max_length=50,  null=True, blank=True)

    def __str__(self):
        return self.role


class College(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    college = models.CharField(
        max_length=50,    null=True, blank=True)

    def __str__(self):
        return f'{self.college} {self.role}'


class Program(models.Model):

    college = models.ForeignKey(College, on_delete=models.CASCADE)
    program = models.CharField(max_length=50,  null=True, blank=True)

    def __str__(self):
        return self.program
