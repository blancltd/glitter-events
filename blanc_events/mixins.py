# -*- coding: utf-8 -*-

import calendar
import datetime
from collections import OrderedDict

from dateutil.relativedelta import relativedelta

from django.utils import timezone

from .models import Category, Event


class EventsMixin(object):
    events_categories = True
    now = timezone.now()
    previous_month = now.replace(day=1) - datetime.timedelta(days=1)
    next_month = now.replace(day=1) + relativedelta(months=1)

    def get_context_data(self, **kwargs):
        context = super(EventsMixin, self).get_context_data(**kwargs)
        context['events_categories'] = self.events_categories
        context['categories'] = Category.objects.all()
        context['event_list'] = self.get_events_list()
        return context

    def get_events_list(self):

        month_days = OrderedDict()
        
        cal = calendar.Calendar(firstweekday=calendar.SUNDAY)
        for week in cal.monthdatescalendar(self.now.year, self.now.month):
            for i in week:
                month_days[i] = []
        
        # Add in existing events
        for event in self.get_queryset():
            event_date = event.start.date()
            month_days[event_date].append(event)
        
        # Calendar events as well
        for i in Event.objects.filter(start__gte=self.now, start__lte=self.next_month):
            event_date = i.start.date()
            month_days[event_date].append(i)
        
        return month_days.items()

    def get_month_total_events_no(self):
        return Event.objects.filter(start__gte=self.now, start__lte=self.next_month).count()

    def get_calendar_day_names(self):
        calendar_days = []
        day_names = list(calendar.day_name)
        cal = calendar.Calendar(firstweekday=calendar.SUNDAY)

        for i in cal.iterweekdays():
            calendar_days.append(day_names[i])

        return calendar_days

