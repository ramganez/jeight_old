from django.db import models
from datetime import datetime

# Create your models here.


class RoomMember(models.Model):
    name = models.CharField(max_length=50,)
    mobile = models.CharField(max_length=12,)
    mail_id = models.EmailField(max_length=75,)
    advance_given = models.DecimalField(max_digits=6, decimal_places=2)
    other_exp_paid = models.DecimalField(max_digits=6, decimal_places=2)
    in_room = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class OtherMember(models.Model):
    name = models.CharField(max_length=50,)
    mobile = models.CharField(max_length=12,)
    mail_id = models.EmailField(max_length=75,)
    check_in = models.DateField(default=datetime.now(), blank=True)
    in_room = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

class MonthlyExpense(models.Model):
    month = models.CharField(max_length=10,
                             default=datetime.now().strftime('%B'))
    rent = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    cable = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    electricity = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    maintenance = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    water = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    last_month_exp = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    next_month_exp = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    grand_total = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    created_on = models.DateTimeField(default=datetime.now(), blank=True)

    def __unicode__(self):
        return self.month


class ShareExpenses(models.Model):
    month = month = models.CharField(max_length=10, default=datetime.now().
                                     strftime('%B'))

    room_member = models.ForeignKey('RoomMember', null=True)
    other_member = models.ForeignKey('OtherMember', null=True)
    amount_to_be_given = models.DecimalField(max_digits=6, decimal_places=2)
    created_on = models.DateTimeField(default=datetime.now(), blank=True)


