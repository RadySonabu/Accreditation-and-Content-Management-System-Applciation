from django.db import models
from django.urls import reverse
from multiselectfield import MultiSelectField
from members.models import MyUser
from django.db.models import Sum
from choices.models import Role, College, Program
from PIL import Image


class AccreditationType(models.Model):

    type_of_accreditations = models.CharField(max_length=150)
    image = models.ImageField(
        upload_to='accreditation_image', blank=True, null=True)

    def __str__(self):
        return self.type_of_accreditations

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height != 200 or img.width != 200:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Forms(models.Model):

    title = models.CharField(
        unique=True, max_length=200, blank=True, null=True)
    type_of_accreditation = models.ForeignKey(
        AccreditationType, on_delete=models.CASCADE)

    year = models.IntegerField()
    college = models.ForeignKey(
        College, on_delete=models.CASCADE, blank=True, null=True)

    created_by = models.ForeignKey(
        MyUser, on_delete=models.CASCADE, null=True, default="")
    created_for = models.ForeignKey(
        Program, on_delete=models.SET_NULL, null=True)
    _total = models.FloatField(default=0, db_column='total')
    _percent = models.FloatField(default=0, db_column='percent')

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse("form-detail", kwargs={"pk": self.pk})

    @property
    def total(self):
        return SubdivisionDetail.objects.filter(subdivision__division__title=self).aggregate(total=Sum("subtotal")).get('total') or 0

    @property
    def percent(self):

        points = SubdivisionDetail.objects.filter(
            subdivision__division__title=self).aggregate(total=Sum("subtotal")).get('total') or 0
        over = SubdivisionDetail.objects.filter(
            subdivision__division__title=self).aggregate(total=Sum("subpoints")).get('total') or 0
        if over == 0:
            return 0
        else:
            percentage = (points/over)*100

        return percentage
    # @property
    # def total(self):
    #     division = self.subdivision_set.only(
    #         'total')
    #     total=0
    #     for division in division:
    #         total += division.total
    #     return total


class Division(models.Model):
    title = models.ForeignKey(Forms, default=1, on_delete=models.CASCADE)
    criteria = models.CharField(unique=True, max_length=150)
    _total = models.FloatField(default=0, db_column='total')

    def __str__(self):
        return self.criteria

    def get_absolute_url(self):
        return reverse("division-detail", kwargs={"pk": self.pk})

    @property
    def total(self):
        return SubdivisionDetail.objects.filter(subdivision__division=self).aggregate(total=Sum("subtotal")).get('total') or 0
    # @property
    # def total(self):
    #     subdivision_detail = self.subdivision_set.only(
    #         '_total')
    #     total = 0
    #     for subdivision_detail in subdivision_detail:
    #         total += subdivision_detail._total
    #         self._total = total

    #     return self._total

    # @total.setter
    # def total(self, value):
    #     print(value + ' ardy')
    #     self._total = value


class Subdivision(models.Model):
    division = models.ForeignKey(
        Division, default=1, on_delete=models.CASCADE)
    criteria = models.CharField(max_length=150,)
    points = models.FloatField()
    _total = models.FloatField(default=0, db_column='total')

    def __str__(self):
        return self.criteria

    def get_absolute_url(self):
        return reverse("subdivision-detail", kwargs={"pk": self.pk})

    @property
    def total(self):
        return self.subdivisiondetail_set.aggregate(total=Sum("subtotal")).get('total') or 0

    # @property
    # def total(self):
    #     subdivision_detail = self.subdivisiondetail_set.only(
    #         'subtotal')
    #     total = 0
    #     for subdivision_detail in subdivision_detail:
    #         total += subdivision_detail.subtotal
    #         self._total = total
    #     return self._total

    # @total.setter
    # def total(self, value):
    #     self._total = value


class SubdivisionDetail(models.Model):
    subdivision = models.ForeignKey(
        Subdivision, default=1, on_delete=models.CASCADE)
    criteria = models.CharField(max_length=150)

    subpoints = models.FloatField(default=0)
    remarks = models.CharField(max_length=150)
    subtotal = models.FloatField(default=0)

    def __str__(self):
        return self.criteria

    def get_absolute_url(self):
        return reverse("subdivisiondetail-detail", kwargs={"pk": self.pk})


class Files(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='uploads', null=True, blank=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs)
