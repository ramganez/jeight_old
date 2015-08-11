import ipdb

# from django.forms import ModelForm
import floppyforms.__future__ as forms

from roomexpenses.models import (MonthlyExpense, RoomMember, OtherMember)

class MonthlyExpenseForm(forms.ModelForm):
    class Meta:
        model = MonthlyExpense
        exclude = ['grand_total', 'created_on']


class RoomMemberForm(forms.ModelForm):
    class Meta:
        model = RoomMember


class OtherMemberForm(forms.ModelForm):
    class Meta:
        model = OtherMember
        labels = {
            'some_amount': 'Rs',
        }



