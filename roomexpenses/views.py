import ipdb
from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.core.urlresolvers import reverse

from roomexpenses.forms import (MonthlyExpenseForm, RoomMemberForm,
                                OtherMemberForm,)
from roomexpenses.models import (ShareExpenses, RoomMember, OtherMember)

# Create your views here.

# FBV
def add_current_month_expenses(request):
    if request.method == "POST":
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

    def get_success_url(self):
        return reverse('current-month-share')

    def form_valid(self, form):
        ipdb.set_trace()
        expenses_data = form.cleaned_data
        grand_total = 0
        for key, value in expenses_data.iteritems():
            if not key == 'month':
                grand_total += float(value)
        room_member_count = RoomMember.objects.filter(in_room=True).count()
        # TODO later
        # other_member_count = OtherMember.objects.filter(in_room=True).count()
        room_member_expense = grand_total/float(room_member_count)

        for obj in RoomMember.objects.all():
            ShareExpenses.objects.create(month=expenses_data['month'],
                                         room_member=obj,
                                         amount_to_be_given=room_member_expense)

        return super(AddCurrentMonthExpenses, self).form_valid(form)


class AddRoomMember(CreateView):
    form_class = RoomMemberForm
    template_name = 'roomexpenses/add_room_member.html'
    success_url = '#'


class AddOtherMember(CreateView):
    form_class = OtherMemberForm
    template_name = 'roomexpenses/add_other_member.html'
    success_url = '#'


class ShowSharedExpenses(TemplateView):
    template_name = "roomexpenses/shared_expenses.html"

    def get_context_data(self, **kwargs):
        context = super(ShowSharedExpenses, self).get_context_data(**kwargs)
        context["share_expenses"] = ShareExpenses.objects.\
            filter(month=datetime.now().strftime('%B'))

        return context



