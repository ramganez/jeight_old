import ipdb

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import (CreateView)

from roomexpenses.forms import (MonthlyExpenseForm, RoomMemberForm,
                                OtherMemberForm)
# Create your views here.

# FBV
def add_current_month_expenses(request):
    if request.method == "POST":
        # ipdb.set_trace()
        form = MonthlyExpenseForm(request.POST)
    if form.is_valid():
        form.save()
        month = form.clean_month()
        return HttpResponse(month + " form valid")
    else:
        form = MonthlyExpenseForm

    return render(request, 'roomexpenses/expense.html', {'form': form})

# CBV
class AddCurrentMonthExpenses(CreateView):
    form_class = MonthlyExpenseForm
    template_name = 'roomexpenses/add_expense.html'
    success_url = '#'



class AddRoomMember(CreateView):
    form_class = RoomMemberForm
    template_name = 'roomexpenses/add_room_member.html'
    success_url = '#'


class AddOtherMember(CreateView):
    form_class = OtherMemberForm
    template_name = 'roomexpenses/add_other_member.html'
    success_url = '#'



