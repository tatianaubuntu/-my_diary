from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from diary.models import Entry


class EntryListView(ListView):
    """Контроллер списка записей"""
    model = Entry
    extra_context = {
        'title': 'Записи'
    }
    paginate_by = 3

    def get_paginate_by(self, queryset):
        """Возвращает список записей по страницам"""
        return self.request.GET.get('paginate_by', self.paginate_by)

