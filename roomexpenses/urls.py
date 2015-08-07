from django.views.generic.base import TemplateView

from django.conf.urls import patterns, include, url
from roomexpenses.views import (AddCurrentMonthExpenses, )
from roomexpenses.views import (AddCurrentMonthExpenses, AddRoomMember,
                                AddOtherMember, ShowSharedExpenses, ListAllMember,
                                UpdateMember)

from roomexpenses import views

urlpatterns = patterns('',
						# url(r'^$', TemplateView.as_view(
						# 	template_name="roomexpenses/home.html"), name='home'),

						url(r'^$', TemplateView.as_view(
							template_name="base.html"), name='home'),

						url(r'^add-expense/$',
							AddCurrentMonthExpenses.as_view(), name='add-month-expenses'),

						url(r'^add-room-member/$', AddRoomMember.as_view(),
							name='add-room-member'),

						url(r'^add-other-member/$', AddOtherMember.as_view(

						), name='add-other-member'),

						url(r'^current-month-share/$',
							ShowSharedExpenses.as_view(), name='current-month-share'),

                        url(r'^list-members/$',
                            ListAllMember.as_view(), name='list-members'),

                        url(r'^update-member/(?P<member_type>\w+)/(?P<member_pk>\d+)/$', UpdateMember.as_view(),
                            name='update-member')

                        )