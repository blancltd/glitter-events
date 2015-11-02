# -*- coding: utf-8 -*-

from dateutil import rrule
from dateutil.relativedelta import relativedelta

from django.utils import timezone

from .models import Event


def sorted_event_list(start_date=None, end_date=None, queryset=None, limit=None):
    # Default start date
    if start_date is None:
        start_date = timezone.now()

    # Default end date
    if end_date is None:
        end_date = start_date + relativedelta(months=+1)

    event_list = []

    # Sort by date
    event_list.sort(key=lambda x: x[0])

    # Limited number of events
    if limit is not None:
        event_list = event_list[:limit]

    return event_list
