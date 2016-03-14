# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, DetailView

from glitter.mixins import GlitterDetailMixin

from .mixins import CalendarMixin, EventsMixin, EventsQuerysetMixin
from .models import Category, Event


class EventDetailView(GlitterDetailMixin, EventsMixin, DetailView):
    model = Event

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        context['current_category'] = self.object.category
        return context


class CategoryEventListView(EventsQuerysetMixin, EventsMixin, ListView):
    template_name_suffix = '_category_list'
    paginate_by = 10

    def get_queryset(self):
        qs = super(CategoryEventListView, self).get_queryset()
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return qs.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super(CategoryEventListView, self).get_context_data(**kwargs)
        context['current_category'] = self.category
        return context


class CalendarCurrentMonthView(CalendarMixin, EventsMixin):
    def get_year(self):
        return str(timezone.now().year)

    def get_month(self):
        return str(timezone.now().month)


class CalendarMonthArchiveView(CalendarMixin, EventsMixin):
    pass
