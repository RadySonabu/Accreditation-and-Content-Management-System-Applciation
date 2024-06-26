from django.db import models
from django.urls import reverse
from multiselectfield import MultiSelectField
from members.models import MyUser
from django.db.models import Sum
from choices.models import Role, College, Program
from PIL import Image
from django.core.validators import MaxValueValidator, MinValueValidator


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

    year = models.PositiveIntegerField()
    college = models.ForeignKey(
        College, on_delete=models.CASCADE, blank=True, null=True)

    created_by = models.ForeignKey(
        MyUser, on_delete=models.CASCADE, null=True, default="")
    created_for = models.ForeignKey(
        Program, on_delete=models.SET_NULL, null=True)
    _total = models.DecimalField(
        default=0, db_column='total', max_digits=7, decimal_places=2)
    _percent = models.DecimalField(
        default=0, db_column='percent',  max_digits=7, decimal_places=2)
    is_active = models.BooleanField(default=False)

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
            percentage=0
            return percentage
        else:
            percentage = (points/over)*100

        return round(percentage)

    @property
    def total_progress_college(self):
        points = SubdivisionDetail.objects.filter(
            subdivision__division__title__college=self.college, subdivision__division__title__year=self.year).aggregate(total=Sum("subtotal")).get('total') or 0

        over = SubdivisionDetail.objects.filter(
            subdivision__division__title__college=self.college, subdivision__division__title__year=self.year).aggregate(total=Sum("subpoints")).get('total') or 0

        if over == 0:
            return 0
        else:
            percentage = (points/over)*100
        return round(percentage)


class Division(models.Model):
    title = models.ForeignKey(Forms, default=1, on_delete=models.CASCADE)
    criteria = models.CharField(unique=True, max_length=150)
    _total = models.DecimalField(
        default=0, db_column='total',  max_digits=7, decimal_places=2)

    def __str__(self):
        return self.criteria

    def get_absolute_url(self):
        return reverse("division-detail", kwargs={"pk": self.pk})

    @property
    def total(self):
        return SubdivisionDetail.objects.filter(subdivision__division=self).aggregate(total=Sum("subtotal")).get('total') or 0


class Subdivision(models.Model):
    division = models.ForeignKey(
        Division, default=1, on_delete=models.CASCADE)
    criteria = models.CharField(max_length=150,)
    _points = models.DecimalField(default=0, validators=[
        MinValueValidator(0.0)],  max_digits=7, decimal_places=2, db_column='points')
    _total = models.DecimalField(
        default=0, db_column='total',  max_digits=7, decimal_places=2)

    def __str__(self):
        return self.criteria

    def get_absolute_url(self):
        return reverse("subdivision-detail", kwargs={"pk": self.pk})

    @property
    def points(self):
        points = SubdivisionDetail.objects.filter(
            subdivision=self).aggregate(total=Sum("subpoints")).get('total') or 0

        return points

    @property
    def total(self):
        total = self.subdivisiondetail_set.aggregate(
            total=Sum("subtotal")).get('total') or 0
        if total > self.points:
            return self.points
        return total


class SubdivisionDetail(models.Model):
    def max_subpoints(self):
        over = SubdivisionDetail.objects.filter(subdivision=self).aggregate(
            total=Sum("subpoints")).get('total') or 0

        return 100
    subdivision = models.ForeignKey(
        Subdivision, default=1, on_delete=models.CASCADE)
    criteria = models.CharField(max_length=150)

    subpoints = models.DecimalField(default=0,  validators=[
        MinValueValidator(0.0)],   max_digits=7, decimal_places=2, )
    remarks = models.CharField(max_length=150)
    subtotal = models.DecimalField(default=0, validators=[
        MinValueValidator(0.0)],  max_digits=7, decimal_places=2)
    can_upload = models.ForeignKey(
        Program, on_delete=models.CASCADE, null=True, )

    def __str__(self):
        return f'{self.criteria}'

    def get_absolute_url(self):
        return reverse("subdivisiondetail-detail", kwargs={"pk": self.pk})

    def get_note(self):

        total = Comment.objects.filter(files__subdivisiondetail_id=self.id)
        count = total.count()
        return count


class Files(models.Model):

    def uploads(self, filename):
        uploads = f'''uploads/{self.subdivisiondetail.subdivision.division.title.year}/{self.subdivisiondetail.subdivision.division.title.type_of_accreditation}/{self.subdivisiondetail.subdivision.division.title.college.college}/{self.subdivisiondetail.subdivision.division.title.created_for}/{self.subdivisiondetail.subdivision.division}/{self.subdivisiondetail.subdivision}/{self.subdivisiondetail}/{self.file}'''
        return uploads

    subdivisiondetail = models.ForeignKey(
        'SubdivisionDetail', on_delete=models.CASCADE, default=1)
    file = models.FileField(upload_to=uploads, null=True,
                            blank=True, max_length=10000)
    filename = models.CharField(max_length=1500)

    def __str__(self):
        return self.filename

    def name(self):
        return self.filename

    def get_absolute_url(self):
        return reverse("file_list", kwargs={"pk": self.pk})

    def get_note(self, **kwargs):

        total = self.comment_set.exclude(comment='')
        count = total.count()
        return count


class Comment(models.Model):

    files = models.ForeignKey(Files, on_delete=models.CASCADE)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.files.filename

    def get_absolute_url(self):
        return reverse("comment-list", kwargs={"pk": self.files.pk})
