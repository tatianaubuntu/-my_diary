from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from diary.forms import EntryForm
from diary.models import Entry
from diary.services import get_cashe_entry_list


class EntryListView(LoginRequiredMixin, ListView):
    """Контроллер списка записей"""
    model = Entry
    extra_context = {
        'title': 'Записи'
    }
    paginate_by = 9

    def get_paginate_by(self, queryset):
        """Возвращает список записей по страницам"""
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_queryset(self):
        """Возвращает список записей в соответствии с поиском"""
        query = self.request.GET.get('search', None)
        object_list = Entry.objects.filter(owner=self.request.user)
        if query:
            object_list = object_list.filter(
                Q(title__icontains=query) | Q(body__icontains=query)
            )
        return object_list

    def get_context_data(self, **kwargs):
        """Возвращает закешированный список записей"""
        context_data = super().get_context_data(**kwargs)
        context_data['entries'] = get_cashe_entry_list()
        return context_data


class EntryDetailView(UserPassesTestMixin, DetailView):
    """Контроллер просмотра одной записи"""
    model = Entry

    def get_context_data(self, **kwargs):
        """Возвращает наименование страницы"""
        context_data = super().get_context_data(**kwargs)
        entry = self.get_object()
        context_data['title'] = entry.title
        return context_data

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user


class EntryCreateView(CreateView):
    """Контроллер создания новой записи"""
    model = Entry
    form_class = EntryForm
    extra_context = {
        'title': 'Создание записи'
    }

    def form_valid(self, form):
        """ Возвращает переход на страницу с записью, после ее создания"""
        entry = form.save()
        user = self.request.user
        entry.owner = user
        entry.save()
        return redirect('diary:entry', pk=entry.pk)


class EntryUpdateView(UserPassesTestMixin, UpdateView):
    """Контроллер изменения записи"""
    model = Entry
    form_class = EntryForm
    extra_context = {
        'title': 'Редактирование записи'
    }

    def get_success_url(self):
        """Возвращает переход на страницу с записью, если форма валидна"""
        return reverse('diary:entry', args=[self.kwargs.get('pk')])

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user


class EntryDeleteView(UserPassesTestMixin, DeleteView):
    """Контроллер удаления записи"""
    model = Entry
    success_url = reverse_lazy('diary:entries')

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user
