from django.urls import path
from diary.apps import DiaryConfig
from diary.views import EntryListView

app_name = DiaryConfig.name

urlpatterns = [
    path('entries/', EntryListView.as_view(), name='entries'),
    #path('blog/<int:pk>', BlogDetailView.as_view(), name='blog'),
    #path('create_blog/', BlogCreateView.as_view(), name='create_blog'),
    #path('update_blog/<int:pk>', BlogUpdateView.as_view(), name='update_blog'),
    #path('delete_blog/<int:pk>', BlogDeleteView.as_view(), name='delete_blog'),
]
