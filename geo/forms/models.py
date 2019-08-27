from django.db import models
from django.urls import reverse
from multiselectfield import MultiSelectField
from members.models import MyUser, Program, College
from django.db.models import Sum


class AccreditationType(models.Model):

    type_of_accreditations = models.CharField(max_length=150)

    def __str__(self):
        return self.type_of_accreditations


class Forms(models.Model):

    title = models.CharField(
        unique=True, max_length=200, blank=True, null=True)
    type_of_accreditation = models.ForeignKey(
        AccreditationType, on_delete=models.CASCADE)

    year = models.CharField(max_length=4)
    college = models.ForeignKey(
        College, on_delete=models.CASCADE, blank=True, null=True)

    created_by = models.ForeignKey(
        MyUser, on_delete=models.CASCADE, null=True, default="")
    created_for = models.ForeignKey(
        Program, on_delete=models.SET_NULL, null=True)
    total = models.FloatField(default=0)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse("form-detail", kwargs={"pk": self.pk})


class Division(models.Model):
    title = models.ForeignKey(Forms, default=1, on_delete=models.CASCADE)
    criteria = models.CharField(unique=True, max_length=150)

    def __str__(self):
        return self.criteria

    def get_absolute_url(self):
        return reverse("division-detail", kwargs={"pk": self.pk})


class Subdivision(models.Model):
    division = models.ForeignKey(
        Division, default=1, on_delete=models.CASCADE)
    criteria = models.CharField(max_length=150,)
    points = models.FloatField()
    total = models.FloatField(default=0)

    def __str__(self):
        return self.criteria

    def get_absolute_url(self):
        return reverse("subdivision-detail", kwargs={"pk": self.pk})

    @property
    def total(self):
        subdivision_detail = self.subdivisiondetail_set.only(
            'subtotal')
        total = 0
        for subdivision_detail in subdivision_detail:
            total += subdivision_detail.subtotal
        return total


class SubdivisionDetail(models.Model):
    subdivision = models.ForeignKey(
        Subdivision, default=1, on_delete=models.CASCADE)
    criteria = models.CharField(max_length=150)

    subpoints = models.FloatField()
    remarks = models.CharField(max_length=150)
    subtotal = models.FloatField()

    def __str__(self):
        return self.criteria

    def get_absolute_url(self):
        return reverse("subdivisiondetail-detail", kwargs={"pk": self.pk})
