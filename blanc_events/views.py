# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views.generic import ListView
from django.views.generic.dates import MonthArchiveView

from .mixins import EventsMixin
from .models import Event, Category


class EventListView(EventsMixin):
    model = Event

    def get_context_data(self, **kwargs):
        context = super(EventListView, self).get_context_data(**kwargs)

        context['total_events'] = self.get_month_total_events_no()
        context['calendar_headings'] = self.get_calendar_day_names()
        context['current_month'] = self.get_current_month()
        return context


class CategoryEventListView(EventsMixin, ListView):
    model = Event

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return self.model.objects.filter(final_date__gte=timezone.now(), category=self.category)

    def get_context_data(self, **kwargs):
        context = super(CategoryEventListView, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context


class CalendarMonthArchiveView(EventsMixin, MonthArchiveView):
    queryset = Event.objects.all()
    date_field = 'start'
    allow_empty = True

    def get_context_data(self, **kwargs):
        context = super(CalendarMonthArchiveView, self).get_context_data(**kwargs)
        context['current_month'] = self.get_current_month()
        return context

    
