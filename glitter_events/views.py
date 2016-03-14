# -*- coding: utf-8 -*-

from datetime import date

from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views.generic import ListView
from django.views.generic.dates import DateDetailView, MonthArchiveView

from glitter.mixins import GlitterDetailMixin

from .mixins import CalendarMixin, CategoryMixin, EventsMixin, EventsQuerysetMixin
from .models import Category, Event


class EventDetailView(GlitterDetailMixin, EventsMixin, DateDetailView):
    model = Event
    month_format = '%m'
    date_field = 'date_url'
    allow_future = True

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        context['current_category'] = self.object.category
        return context


class CalendarCurrentMonthView(CalendarMixin, EventsMixin, MonthArchiveView):
    def get_year(self):
        return str(timezone.now().year)

    def get_month(self):
        return str(timezone.now().month)


class CalendarMonthArchiveView(CalendarMixin, EventsMixin, MonthArchiveView):
    pass


class EventListView(EventsQuerysetMixin, ListView):
    paginate_by = 10

    def get_queryset(self):
        qs = super(EventListView, self).get_queryset()
        return qs.filter(start__gte=date.today())


class EventListArchiveView(EventsQuerysetMixin, ListView):
    paginate_by = 10
    template_name_suffix = '_list_archive'

    def get_queryset(self):
        qs = super(EventListArchiveView, self).get_queryset()
        return qs.filter(start__lt=date.today()).order_by('-start')


class EventListCategoryView(CategoryMixin, EventListView):
    template_name_suffix = '_list_category'

    def get_queryset(self):
        qs = super(EventListCategoryView, self).get_queryset()
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return qs.filter(category=self.category)


class EventListCategoryArchiveView(CategoryMixin, EventListArchiveView):
    template_name_suffix = '_list_category_archive'

    def get_queryset(self):
        qs = super(EventListCategoryArchiveView, self).get_queryset()
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return qs.filter(category=self.category)
