from django.db import models

# Create your models here.
class BuyerJobBuyerA00(models.Model):
    job_buyer_a00_rec = models.AutoField(primary_key=True)
    job_buyer_id = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.TextField()
    budgeted_amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=11)
    notes = models.TextField()
    active_status = models.BooleanField()
    owner_contact_id_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'buyer_job_buyer_a00'


class BuyerJobBuyerA01(models.Model):
    job_buyer_a01_rec = models.AutoField(primary_key=True)
    job_skills_id = models.CharField(max_length=50)
    skill_id = models.IntegerField()
    skill_description = models.CharField(max_length=14)
    notes = models.TextField()
    active_status = models.BooleanField()
    job_buyer_id = models.ForeignKey(BuyerJobBuyerA00, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'buyer_job_buyer_a01'


class BuyerJobBuyerA02(models.Model):
    job_buyer_a02_rec = models.AutoField(primary_key=True)
    bid_invite_id = models.CharField(max_length=50)
    group_id_id = models.IntegerField()
    status = models.CharField(max_length=11)
    notes = models.TextField()
    active_status = models.BooleanField()
    job_buyer_id = models.ForeignKey(BuyerJobBuyerA00, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'buyer_job_buyer_a02'


class BuyerJobBuyerA03(models.Model):
    job_buyer_a03_rec = models.AutoField(primary_key=True)
    bid_id = models.CharField(max_length=50)
    bidder_reference_id = models.CharField(db_column='bidder_reference_Id', max_length=50)  # Field name made lowercase.
    group_id_id = models.IntegerField()
    job_skills_id = models.CharField(max_length=50)
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=11)
    notes = models.TextField()
    active_status = models.BooleanField()
    job_buyer_id = models.ForeignKey(BuyerJobBuyerA00, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'buyer_job_buyer_a03'


class JobJobA00(models.Model):
    job_a00_rec = models.AutoField(primary_key=True)
    awarded_job_id = models.CharField(max_length=50)
    group_id_id = models.IntegerField()
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=9)
    notes = models.TextField()
    active_status = models.BooleanField()
    bid_id = models.ForeignKey(BuyerJobBuyerA03, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'job_job_a00'


class JobJobA01(models.Model):
    job_a01_rec = models.AutoField(primary_key=True)
    milestone_id = models.CharField(max_length=50)
    due_date = models.DateField()
    status = models.CharField(max_length=9)
    notes = models.TextField()
    active_status = models.BooleanField()
    awarded_job_id = models.ForeignKey(JobJobA00, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'job_job_a01'


class ProviderJobProviderA00(models.Model):
    job_provider_a00_rec = models.AutoField(primary_key=True)
    job_provider_id = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    group_id_id = models.IntegerField()
    notes = models.TextField()
    active_status = models.BooleanField()
    job_buyer_id = models.ForeignKey(BuyerJobBuyerA00, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'provider_job_provider_a00'


class ProviderJobProviderA01(models.Model):
    job_provider_a01_rec = models.AutoField(primary_key=True)
    job_bid_reference_id = models.CharField(max_length=50)
    datetimestamp = models.DateTimeField()
    group_id = models.CharField(max_length=50)
    notes = models.TextField()
    active_status = models.BooleanField()
    bid_id = models.ForeignKey(BuyerJobBuyerA03, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'provider_job_provider_a01'