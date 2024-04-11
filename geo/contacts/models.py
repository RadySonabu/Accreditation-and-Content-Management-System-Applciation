from django.db import models
from django.contrib.auth.models import User


import re


class AccountsRefA01(models.Model):
    ref_a01_rec = models.AutoField(primary_key=True)
    ref_deductions_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    percentage = models.DecimalField(max_digits=4, decimal_places=2)
    comments = models.TextField()
    active_status = models.BooleanField()
    max_perc = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'accounts_ref_a01'

    def __str__(self):
        return self.name
    
class ContactContactA00(models.Model):
    contact_a00_rec = models.AutoField(primary_key=True)
    contact_id = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_initial = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address_1 = models.CharField(max_length=50)
    barangay_district = models.CharField(max_length=50)
    city_municipality = models.CharField(max_length=50)
    postal_code = models.IntegerField()
    province = models.CharField(max_length=50)
    phone_1 = models.CharField(max_length=31)
    phone_2 = models.CharField(blank=True,max_length=31)
    email = models.CharField(unique=True, max_length=254)
    active_status = models.BooleanField()
    date_created = models.DateTimeField(blank=True, null=True)
    created_by_id = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'contact_contact_a00'

    def __str__(self):
        return f'{self.created_by_id} Email: {self.email} | Name:{self.first_name} {self.last_name} | {self.contact_id}'
    
    

class ContactContactA01(models.Model):
    contact_a01_rec = models.AutoField(primary_key=True)
    skill_id = models.IntegerField()
    comments = models.TextField()
    date_created = models.DateTimeField(blank=True, null=True)
    active_status = models.BooleanField()
    contact_id = models.ForeignKey(ContactContactA00, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'contact_contact_a01'

    def __str__(self):
        return f'Contact: {self.contact_id} | {self.skill_id}'
        
class ContactContactA02(models.Model):
    contact_a02_rec = models.AutoField(primary_key=True)
    endorsement_id = models.IntegerField()
    message = models.TextField()
    date_created = models.DateTimeField(blank=True, null=True)
    active_status = models.BooleanField()
    contact_id = models.ForeignKey(ContactContactA00, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'contact_contact_a02'


class ContactContactA03(models.Model):
    contact_a03_rec = models.AutoField(primary_key=True)
    sample_work_id = models.CharField(max_length=50)
    file_name = models.CharField(max_length=50)
    comments = models.TextField()
    active_status = models.BooleanField()
    date_created = models.DateTimeField(blank=True, null=True)
    contact_id = models.ForeignKey(ContactContactA00, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'contact_contact_a03'

class ContactContactA04(models.Model):
    contact_a04_rec = models.AutoField(primary_key=True)
    contact_deduction_id = models.CharField(max_length=50)
    comments = models.TextField()
    active_status = models.BooleanField()
    date_created = models.DateTimeField(blank=True, null=True)
    contact_id = models.ForeignKey(ContactContactA00, models.DO_NOTHING)
    deduction_id_id = models.ForeignKey(AccountsRefA01, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'contact_contact_a04'

class ContactGroupA00(models.Model):
    AGENT_CHOICES = (
        ('Individual','Individual'),
        ('Team', 'Team')
    )
    group_a00_rec = models.AutoField(primary_key=True)
    group_id = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    address_1 = models.CharField(max_length=50)
    barangay_district = models.CharField(max_length=50)
    city_municipality = models.CharField(max_length=50)
    postal_code = models.IntegerField()
    province = models.CharField(max_length=50)
    phone_1 = models.CharField(max_length=31)
    phone_2 = models.CharField(max_length=31)
    email = models.CharField(unique=True, max_length=254)
    agent = models.CharField(max_length=50, choices=AGENT_CHOICES)
    active_status = models.BooleanField()
    date_created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contact_group_a00'

    def __str__(self):
        return self.name
    

class ContactGroupA01(models.Model):
    group_a01_rec = models.AutoField(primary_key=True)
    group_role = models.CharField(max_length=50)
    comments = models.TextField()
    active_status = models.BooleanField()
    date_created = models.DateTimeField(blank=True, null=True)
    contact_id = models.ForeignKey(ContactContactA00, models.DO_NOTHING)
    group_id = models.ForeignKey(ContactGroupA00, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'contact_group_a01'