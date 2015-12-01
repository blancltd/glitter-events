# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from blanc_pages.mixins import BlancPageDetailMixin

from .mixins import EventsMixin, EventsQuerysetMixin
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


class CategoryEventListView(EventsQuerysetMixin, ListView):
    template_name_suffix = '_category_list'
    paginate_by = 10

    def get_queryset(self):
        qs = super(CategoryEventListView, self).get_queryset()
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return qs.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super(CategoryEventListView, self).get_context_data(**kwargs)
        context['current_category'] = self.category
        context['events_categories'] = True
        context['categories'] = Category.objects.all()
        return context


class CalendarMonthArchiveView(EventsMixin):
    pass
