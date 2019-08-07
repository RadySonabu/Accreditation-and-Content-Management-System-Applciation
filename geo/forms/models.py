from django.db import models
from django.urls import reverse


class AccreditationType(models.Model):
    ACCREDITATION_TYPE_CHOICES = (
        ('ABET', 'American Based Education and Technology'),
        ('SA', 'Seoul Accord'),
        ('COE', 'Center of Excellence'),
        ('COD', 'Center of Development'),
        ('FP', 'FAAP-PACUCOA'),
        ('PA', 'PTC-ACBET'),
        ('PP', 'PCS-PCAB')
    )
    form_type = models.CharField(
        choices=ACCREDITATION_TYPE_CHOICES, max_length=100)

    def __str__(self):
        return self.form_type


class BasicInfo(models.Model):

    # PACUCOA_LEVEL_CHOICES = (
    #     ('I', 'Level I'),
    #     ('II', 'Level II'),
    #     ('III', 'Level III'),
    #     ('IV', 'Level IV'),
    # )
    COLLEGE_CHOICES = (
        ('CITE', 'College of Information Technology Education'),
        ('CEA', 'College of Engineering and Architecture'),
        ('CBE', 'College of Business Education'),
        ('COA', 'College of Arts'),
        ('CME', 'College of Maritime Education'),
        ('N/A', 'Not Applicable')
    )
    BRANCH_CHOICES = (
        ('MNL', 'Manila Branch'),
        ('QC', 'Quezon City Branch'),
    )
    accreditation_type = models.ForeignKey(
        AccreditationType, on_delete=models.CASCADE)  # primary key is passed here!
    branch = models.CharField(choices=BRANCH_CHOICES, max_length=100)
    year = models.CharField(max_length=4)
    college = models.CharField(choices=COLLEGE_CHOICES, max_length=100)
    address = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    middle_initial = models.CharField(max_length=2)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.accreditation_type } infos'


class SubdivisionDetail(models.Model):

    criteria = models.CharField(max_length=150)
    points = models.FloatField()
    subpoints = models.FloatField()
    remarks = models.CharField(max_length=150)
    subtotal = models.FloatField()
    total = models.FloatField()

    def __str__(self):
        return self.criteria


class Subdivision(models.Model):
    subdivision_detail = models.ForeignKey(
        SubdivisionDetail, on_delete=models.CASCADE)
    criteria = models.CharField(max_length=150)
    points = models.FloatField()

    def __str__(self):
        return f'{ self.criteria} with {self.points} points'


class Division(models.Model):
    subdivision_detail = models.ForeignKey(
        SubdivisionDetail, on_delete=models.CASCADE)
    subdivision = models.ForeignKey(Subdivision, on_delete=models.CASCADE)
    criteria = models.CharField(max_length=150)

    def __str__(self):
        return self.criteria


class Forms(models.Model):
    ACCREDITATION_TYPE_CHOICES = (
        ('ABET', 'American Based Education and Technology'),
        ('SA', 'Seoul Accord'),
        ('COE', 'Center of Excellence'),
        ('COD', 'Center of Development'),
        ('FP', 'FAAP-PACUCOA'),
        ('PA', 'PTC-ACBET'),
        ('PP', 'PCS-PCAB')
    )
    COLLEGE_CHOICES = (
        ('CITE', 'College of Information Technology Education'),
        ('CEA', 'College of Engineering and Architecture'),
        ('CBE', 'College of Business Education'),
        ('COA', 'College of Arts'),
        ('CME', 'College of Maritime Education'),
        ('N/A', 'Not Applicable')
    )
    BRANCH_CHOICES = (
        ('MNL', 'Manila Branch'),
        ('QC', 'Quezon City Branch'),
    )
    title = models.CharField(max_length=50)

    form_type = models.CharField(
        choices=ACCREDITATION_TYPE_CHOICES, max_length=100)  # primary key is passed here!
    branch = models.CharField(choices=BRANCH_CHOICES, max_length=100)
    year = models.CharField(max_length=4)
    college = models.CharField(choices=COLLEGE_CHOICES, max_length=100)
    address = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    middle_initial = models.CharField(max_length=2)
    last_name = models.CharField(max_length=50)

    division = models.ForeignKey(Division, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.division}'
