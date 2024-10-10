from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from diary.forms import EntryForm
from diary.models import Entry


class EntryListView(ListView):
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
        if query:
            object_list = Entry.objects.filter(
                Q(title__icontains=query) | Q(body__icontains=query)
            )
        else:
            object_list = Entry.objects.all()
        return object_list


class EntryDetailView(DetailView):
    """Контроллер просмотра одной записи"""
    model = Entry

    def get_context_data(self, **kwargs):
        """Возвращает наименование страницы"""
        context_data = super().get_context_data(**kwargs)
        entry = self.get_object()
        context_data['title'] = entry.title
        return context_data


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
        # user = self.request.user
        # entry.owner = user
        entry.save()
        return redirect('diary:entry', pk=entry.pk)


class EntryUpdateView(UpdateView):
    """Контроллер изменения записи"""
    model = Entry
    form_class = EntryForm
    extra_context = {
        'title': 'Редактирование записи'
    }

    def get_success_url(self):
        """Возвращает переход на страницу с записью, если форма валидна"""
        return reverse('diary:entry', args=[self.kwargs.get('pk')])


class EntryDeleteView(DeleteView):
    """Контроллер удаления записи"""
    model = Entry
    success_url = reverse_lazy('diary:entries')
