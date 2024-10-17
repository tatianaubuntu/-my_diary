from django.urls import path
from django.views.decorators.cache import cache_page

from diary.apps import DiaryConfig
from diary.views import EntryListView, EntryDetailView, EntryCreateView, EntryUpdateView, EntryDeleteView

app_name = DiaryConfig.name

urlpatterns = [
    path('entries/', EntryListView.as_view(), name='entries'),
    path('entry/<int:pk>', EntryDetailView.as_view(), name='entry'),
    path('create_entry/', EntryCreateView.as_view(), name='create_entry'),
    path('update_entry/<int:pk>', EntryUpdateView.as_view(), name='update_entry'),
    path('delete_entry/<int:pk>', EntryDeleteView.as_view(), name='delete_entry'),
]
