from django.urls import path
from . import views as clkview
urlpatterns=[
    path('',clkview.home),
]