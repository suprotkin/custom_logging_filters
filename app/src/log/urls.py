from .views import LogView, LogFilterView
from django.urls import path

app_name = 'log'

urlpatterns = [
    path('', LogView.as_view(), name='log'),
    path('filter/', LogFilterView.as_view(), name='set_filter'),
]
