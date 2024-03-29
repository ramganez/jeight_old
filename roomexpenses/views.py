import ipdb
from datetime import datetime
import itertools

from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.generic import (CreateView, TemplateView, ListView,
                                  UpdateView)
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


def calculate_shareExpenses():
    pass


# CBV
class AddCurrentMonthExpenses(CreateView):
    form_class = MonthlyExpenseForm
    template_name = 'roomexpenses/add_expense.html'

    def get_success_url(self):
        return reverse('current-month-share')

    def form_valid(self, form):
        ipdb.set_trace()

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

        # updating multiple objects at once
        # if last created share expense was duplicate
        ShareExpenses.objects.filter(month=expenses_data['month']).update(is_duplicate=True)

        choice_all_count = (RoomMember.objects.filter(in_room=True).count()+
                            OtherMember.objects.filter(in_room=True, ready_to_share='all').count())

        choice_rent_count = (OtherMember.objects.filter(in_room=True, ready_to_share='rent').count())

        choice_food_count = (OtherMember.objects.filter(in_room=True, ready_to_share='food').count())

        rental_expense_share = float(rental_expense)/choice_all_count
        room_expense_share = float(room_expense)/(choice_all_count+
                                                  choice_rent_count+
                                                  choice_food_count)

        #reduce from some amount
        total_some_amount = 0
        for other_mem in OtherMember.objects.filter(in_room=True, ready_to_share='some_amount'):
            total_some_amount += other_mem.some_amount
        reduce_some_amount = float(total_some_amount)/choice_all_count

        for obj in RoomMember.objects.filter(in_room=True):
            ShareExpenses.objects.create(month=expenses_data['month'],
                                         room_member=obj,
                                         room_member_share=(
                                             (rental_expense_share+room_expense_share)-reduce_some_amount))

        if OtherMember.objects.filter(in_room=True):
            for obj in OtherMember.objects.filter(in_room=True):
                    # all Share
                    if obj.ready_to_share == 'all':
                        ShareExpenses.objects.create(month=expenses_data['month'],
                                                     other_member=obj,
                                                     other_member_share=((rental_expense_share+room_expense_share)
                                                                         -reduce_some_amount))
                    # rent
                    if obj.ready_to_share == 'rent':
                        ShareExpenses.objects.create(month=expenses_data['month'],
                                                     other_member=obj,
                                                     other_member_share=(rental_expense_share))

                    # food
                    if obj.ready_to_share == 'food':
                        ShareExpenses.objects.create(month=expenses_data['month'],
                                                     other_member=obj,
                                                     other_member_share=(room_expense_share))

                    # none
                    if obj.ready_to_share == 'none':
                        ShareExpenses.objects.create(month=expenses_data['month'],
                                                     other_member=obj,
                                                     other_member_share=0)


        return super(AddCurrentMonthExpenses, self).form_valid(form)


class AddRoomMember(CreateView):
    form_class = RoomMemberForm
    template_name = 'roomexpenses/add_room_member.html'


class AddOtherMember(CreateView):
    form_class = OtherMemberForm
    template_name = 'roomexpenses/add_other_member.html'


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


class UpdateMember(UpdateView):
    template_name = 'roomexpenses/update_members.html'
    pk_url_kwarg = 'member_pk'
    slug_url_kwarg = 'member_type'

    kwarg_map = {
        'permanent': RoomMember.objects.all(),
        'temporary': OtherMember.objects.all()
    }

    # override this method for update the members in on CSV
    def get_object(self, queryset=None, **kwargs):
        # ipdb.set_trace()

        slug = self.kwargs.get(self.slug_url_kwarg)
        queryset = self.kwarg_map.get(slug)
        pk = self.kwargs.get(self.pk_url_kwarg)
        obj = queryset.get(pk=pk)
        return obj