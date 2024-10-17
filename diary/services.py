from django.conf import settings
from django.core.cache import cache

from diary.models import Entry


def get_cashe_entry_list():
    """Возвращает закешированный список записей"""
    if settings.CACHE_ENABLED:
        key = 'entry_list'
        entry_list = cache.get(key)
        if entry_list is None:
            entry_list = Entry.objects.all()
            cache.set(key, entry_list)
    else:
        entry_list = Entry.objects.all()

    return entry_list


def get_cashe_entry(pk):
    """Возвращает закешированную запись"""
    if settings.CACHE_ENABLED:
        key = 'entry'
        entry = cache.get(key)
        if entry is None:
            entry = Entry.objects.get(pk=pk)
            cache.set(key, entry)
    else:
        entry = Entry.objects.get(pk=pk)

    return entry
