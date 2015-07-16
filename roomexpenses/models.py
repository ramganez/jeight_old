from datetime import datetime

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class RoomMember(models.Model):
    name = models.CharField(max_length=50,)
    mobile = models.CharField(max_length=12,)
    mail_id = models.EmailField(max_length=75,)
    advance_given = models.DecimalField(max_digits=6, decimal_places=2)
    other_exp_paid = models.DecimalField(max_digits=6, decimal_places=2)
    in_room = models.BooleanField(default=True)

    def clean(self):
        """extra whitespace will be stripped"""
        if self.name:
            self.name = self.name.strip()

    def get_absolute_url(self):
        return reverse('list-members')

    def __unicode__(self):
        return self.name


class OtherMember(models.Model):
    name = models.CharField(max_length=50,)
    mobile = models.CharField(max_length=12, null=True, blank=True)
    mail_id = models.EmailField(max_length=75, null=True, blank=True)
    check_in = models.DateField(default=datetime.now)
    in_room = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

class MonthlyExpense(models.Model):
    month = models.CharField(max_length=10,
                             default=datetime.now().strftime('%B'))
    rent = models.DecimalField(max_digits=7, decimal_places=2, default=7500)
    cable = models.DecimalField(max_digits=7, decimal_places=2, default=100) 
    electricity = models.DecimalField(max_digits=7, decimal_places=2,
                                      default=0)
    maintenance = models.DecimalField(max_digits=7, decimal_places=2,
                                      default=350)
    water = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    last_month_exp = models.DecimalField(max_digits=7, decimal_places=2,
                                         default=0)
    next_month_exp = models.DecimalField(max_digits=7, decimal_places=2,
                                         default=0)
    grand_total = models.DecimalField(max_digits=7, decimal_places=2,
                                      null=True)
    created_on = models.DateTimeField(default=datetime.now)


    def __unicode__(self):
        return self.month


class ShareExpenses(models.Model):
    month = month = models.CharField(max_length=10, default=datetime.now().
                                     strftime('%B'))

    room_member = models.ForeignKey('RoomMember', null=True)
    other_member = models.ForeignKey('OtherMember', null=True)
    room_member_share = models.DecimalField(max_digits=6, decimal_places=2,
                                            null=True)
    other_member_share = models.DecimalField(max_digits=6, decimal_places=2,
                                             null=True)
    is_duplicate = models.BooleanField(default=False)
    created_on = models.DateTimeField(default=datetime.now, blank=True)


    def __unicode__(self):
        return self.created_on.strftime('%H-%M-%S')



