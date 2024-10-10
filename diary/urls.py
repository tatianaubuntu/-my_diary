from django.urls import path
from django.views.decorators.cache import cache_page

from diary.apps import DiaryConfig
from diary.views import EntryListView, EntryDetailView, EntryCreateView, EntryUpdateView, EntryDeleteView

app_name = DiaryConfig.name

urlpatterns = [
    path('entries/', cache_page(60)(EntryListView.as_view()), name='entries'),
    path('entry/<int:pk>', cache_page(60)(EntryDetailView.as_view()), name='entry'),
    path('create_entry/', EntryCreateView.as_view(), name='create_entry'),
    path('update_entry/<int:pk>', cache_page(60)(EntryUpdateView.as_view()), name='update_entry'),
    path('delete_entry/<int:pk>', EntryDeleteView.as_view(), name='delete_entry'),
]
