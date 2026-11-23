from django.urls import path

from . import views

urlpatterns = [
    path("",views.index_view),
    path("add/",views.add_view),
    path("list/",views.list_view)
]