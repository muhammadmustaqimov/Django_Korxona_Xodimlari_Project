from django.urls import path
from .views import (
    XodimDetailView,
    XodimListView,
    XodimCreateView,
    XodimUpdateView,
    XodimDeleteView,
    main

)

from . import views

urlpatterns = [
    path('post/<int:pk>/delete', XodimDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit', XodimUpdateView.as_view(), name='post_edit'),
    path('post/new/', XodimCreateView.as_view(), name='post_new'),
    path('', XodimListView.as_view(), name='home'),
    path('post/<int:pk>/',  XodimDetailView.as_view(), name='post_detail'),
    path('1', main, name='1' )
]