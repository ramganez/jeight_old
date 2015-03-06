from django.db import models
import datetime

# Create your models here.


class RoomMember(models.Model):
    name = models.CharField(max_length=50,)
    mobile = models.CharField(max_length=12,)
    mail_id = models.EmailField(max_length=75,)
    advance_given = models.DecimalField(max_digits=6,decimal_places=2)
    other_exp_paid = models.DecimalField(max_digits=6,decimal_places=2)

    def __unicode__(self):
        return self.name


class OtherMember(models.Model):
    name = models.CharField(max_length=50,)
    mobile = models.CharField(max_length=12,)
    mail_id = models.EmailField(max_length=75,)
    check_in = models.DateField(default=datetime.date.today)

    def __unicode__(self):
        return self.name

class MonthlyExpense(models.Model):
    month = models.CharField(max_length=10,\
        default=datetime.datetime.now().strftime('%B'))
    rent = models.DecimalField(max_digits=7,decimal_places=2)
    cable = models.DecimalField(max_digits=5,decimal_places=2)
    electricity = models.DecimalField(max_digits=5,decimal_places=2)
    last_month_exp = models.DecimalField(max_digits=7,decimal_places=2)
    next_month_exp = models.DecimalField(max_digits=7,decimal_places=2)
    grand_total = models.DecimalField(max_digits=7,decimal_places=2, null=True)

    def __unicode__(self):
    	return self.month

