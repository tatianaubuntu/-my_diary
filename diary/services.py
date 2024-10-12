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
