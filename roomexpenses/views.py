import ipdb
from datetime import datetime
import itertools

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (CreateView, TemplateView, ListView)
from django.core.urlresolvers import reverse

from roomexpenses.forms import (MonthlyExpenseForm, RoomMemberForm,
                                OtherMemberForm,)
from roomexpenses.models import (ShareExpenses, RoomMember, OtherMember)

# Create your views here.


# FBV for test
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
        # ipdb.set_trace()

        # TODO later write single function
        expenses_data = form.cleaned_data
        rental_expense = 0
        room_expense = 0
        grand_total = 0

        for_rental_expense = ['rent', 'maintenance']
        for_room_expense = ['cable', 'electricity', 'water',
                            'last_month_exp', 'next_month_exp']

        for key, value in expenses_data.iteritems():
            if not key == 'month':
                grand_total += float(value)
                if key in for_rental_expense:
                    rental_expense += float(value)
                if key in for_room_expense:
                    room_expense += float(value)

        room_member_count = RoomMember.objects.filter(in_room=True).count()
        other_member_count = OtherMember.objects.filter(in_room=True).count()

        rental_expense_share = rental_expense/float(room_member_count)
        room_expense_share = room_expense/(float(
            room_member_count)+float(other_member_count+room_member_count))

        # updating multiple objects at once
        # if last created share expense was duplicate
        ShareExpenses.objects.filter(month=expenses_data['month']).update(is_duplicate=True)

        for obj in RoomMember.objects.filter(in_room=True):
            ShareExpenses.objects.create(month=expenses_data['month'],
                                         room_member=obj,
                                         room_member_share=(
                                             rental_expense_share+room_expense_share))

        if OtherMember.objects.filter(in_room=True):
            for obj in OtherMember.objects.filter(in_room=True):
                    ShareExpenses.objects.create(month=expenses_data['month'],
                                                 other_member=obj,
                                                 other_member_share=room_expense_share)

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
            filter(month=datetime.now().strftime('%B'), is_duplicate=False)

        return context


class ListRoomMember(ListView):
    # model = RoomMember
    template_name = 'roomexpenses/list_members.html'

    def get_queryset(self):
        """Returns Members they are available room"""
        return RoomMember.objects.filter(in_room=True)


class ListOtherMember(ListView):
    model = OtherMember
    template_name = 'roomexpenses/list_members.html'

    def get_queryset(self):
        """Returns Members they are available room"""
        return OtherMember.objects.filter(in_room=True)


class ListAllMember(ListView):
    template_name = 'roomexpenses/list_members.html'

    def get_queryset(self):
        """Returns Members they are available room"""
        return RoomMember.objects.filter(in_room=True)

    def get_context_data(self, **kwargs):
        """ Return Room member list
            and Other member list
        """
        context = super(ListView, self).get_context_data(**kwargs)
        zip_members = itertools.izip_longest(RoomMember.objects.filter(in_room=True),
                                             OtherMember.objects.filter(in_room=True), fillvalue='')

        context['zip_members'] = zip_members

        return context