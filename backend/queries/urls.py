from django.urls import path, include
from login import urls
from . import views

urlpatterns = [
    path('new/', views.new_query, name='newquery'),
    path('show_active/', views.show_active_queries, name='show active queries'),
    path('remove/', views.remove_query, name="remove query"),
    # path('show_accepted/', views.show_accepted_queries, name='show accepted queries'),
    path('accept/', views.accept_query, name='accepted query'),
    path('show_status/', views.show_status, name='show_status')
]
