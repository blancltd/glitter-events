# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        r'^$',
        views.EventListView.as_view(),
        name='list'
    ),

    url(
        r'^(?P<year>[0-9]{4})/(?P<month>[0-9]+)/(?P<day>[0-9]+)/(?P<slug>[-\w]+)/$',
        views.EventDetailView.as_view(),
        name='detail'
    ),

    url(
        r'^category/(?P<slug>[-\w]+)/$',
        views.CategoryEventListView.as_view(),
        name='category-event-list'
    ),
    url(
        r'^calendar/(?P<year>\d{4})/(?P<month>\d{2})/$',
        views.CalendarMonthArchiveView.as_view(month_format='%m'),
        name='calendar-month'
    ),
]

