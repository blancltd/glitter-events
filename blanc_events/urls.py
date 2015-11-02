# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

import views


urlpatterns = patterns(
    '',
    url(
        r'^$',
        views.EventListView.as_view(),
        name='list'
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
)

