from django.urls import path # type: ignore
from .views import IndexView

urlpatterns = [
    path('',IndexView.as_view(),name='index'),
]