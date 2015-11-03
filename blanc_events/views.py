# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, DetailView

from blanc_pages.mixins import BlancPageDetailMixin

from .mixins import EventsMixin
from .models import Event, Category


class EventListView(EventsMixin):
    pass


class EventDetailView(BlancPageDetailMixin, DetailView):
    model = Event

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['current_category'] = self.object.category
        context['events_categories'] = True
        return context


class CategoryEventListView(EventsMixin, ListView):
    template_name_suffix = '_list'
    model = Event

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return self.model.objects.filter(final_date__gte=timezone.now(), category=self.category)

    def get_context_data(self, **kwargs):
        context = super(CategoryEventListView, self).get_context_data(**kwargs)
        context['current_category'] = self.category
        return context


class CalendarMonthArchiveView(EventsMixin):
    pass

    

