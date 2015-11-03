# -*- coding: utf-8 -*-

import calendar
import datetime
from collections import OrderedDict

from django.utils import timezone
from django.views.generic.dates import MonthArchiveView
from django.http import Http404

from .models import Category, Event


class EventsMixin(MonthArchiveView):
    events_categories = True
    allow_future = True
    allow_empty = True
    model = Event
    year_format = '%Y'
    month_format = '%m'
    date_field = 'start'

    def get_year(self):
        """
        Return the year for which this view should display data.
        """
        year = self.year
        if year is None:
            try:
                year = self.kwargs['year']
            except KeyError:
                try:
                    year = self.request.GET['year']
                except KeyError:
                    year = str(self.get_time_now().year)
        return year

    def get_month(self):
        """
        Return the month for which this view should display data.
        """
        month = self.month
        if month is None:
            try:
                month = self.kwargs['month']
            except KeyError:
                try:
                    month = self.request.GET['month']
                except KeyError:
                    month = str(self.get_time_now().month)
        return month

    def get_time_now(self):
        return timezone.now()

    def get_current_month(self):
        if 'month' in self.kwargs:
            if self.get_year() and self.get_month():
                date = datetime.date(int(self.get_year()), int(self.get_month()), 1)
        else:
            date = self.get_time_now().replace(day=1)
        return date

    def get_context_data(self, **kwargs):
        context = super(EventsMixin, self).get_context_data(**kwargs)
        current_month = self.get_current_month()
        now = self.get_time_now()
        current_month = self.get_current_month()
        previous_month = self.get_previous_month(current_month)
        next_month = self.get_next_month(current_month)
        context['events_categories'] = self.events_categories
        context['categories'] = Category.objects.all()
        context['event_list'] = self.get_events_list()
        context['now_month'] = now
        context['previous_month'] = previous_month
        context['next_month'] = next_month
        return context

    def get_events_list(self):
        current_month = self.get_current_month()
        next_month = self.get_next_month(current_month)

        month_days = OrderedDict()
        
        cal = calendar.Calendar(firstweekday=calendar.SUNDAY)
        for week in cal.monthdatescalendar(current_month.year, current_month.month):
            for i in week:
                month_days[i] = []
        
        # Calendar events as well
        for i in self.model.objects.filter(start__gte=current_month, start__lte=next_month):
            event_date = i.start.date()
            month_days[event_date].append(i)
        
        return month_days.items()

    def get_month_total_events_no(self):
        now = self.get_time_now()
        next_month = self.get_next_month(now)
        return Event.objects.filter(start__gte=now, start__lte=next_month).count()

    def get_calendar_day_names(self):
        calendar_days = []
        day_names = list(calendar.day_name)
        cal = calendar.Calendar(firstweekday=calendar.SUNDAY)

        for i in cal.iterweekdays():
            calendar_days.append(day_names[i])

        return calendar_days

