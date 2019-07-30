from django.db import models

class CreateForm(models.Model):
    ACCREDITATION_TYPE_CHOICES = (
        ('ABET', 'American Based Education and Technology'),
        ('SA', 'Seoul Accord'),
        ('COE', 'Center of Excellence'),
        ('COD', 'Center of Development'),
        ('FP', 'FAAP-PACUCOA'),
        ('PA', 'PTC-ACBET'),
        ('PP', 'PCS-PCAB')
    )
    PACUCOA_LEVEL_CHOICES = (
        ('I', 'Level I'),
        ('II', 'Level II'),
        ('III', 'Level III'),
        ('IV', 'Level IV'),
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

    form_id = models.CharField(primary_key=True, max_length=2)
    form_type = models.CharField(choices=ACCREDITATION_TYPE_CHOICES, max_length=100)
    branch = models.CharField(choices=BRANCH_CHOICES, max_length=100)
    year = models.CharField(max_length=4)
    college = models.CharField(choices=COLLEGE_CHOICES, max_length=100)
    address = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    middle_initial = models.CharField(max_length=2)
    last_name = models.CharField(max_length=50)



    def __str__(self):
        return f'{self.form_id}'