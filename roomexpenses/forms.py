import ipdb

from django.forms import ModelForm
from roomexpenses.models import (MonthlyExpense, RoomMember,
                                    OtherMember)

class MonthlyExpenseForm(ModelForm):
    class Meta:
        model = MonthlyExpense
        exclude = ['grand_total']

class RoomMemberForm(ModelForm):
    class Meta:
        model = RoomMember


class OtherMemberForm(ModelForm):
    class Meta:
        model = OtherMember



