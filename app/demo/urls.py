from django.urls import path
from . import views

urlpatterns = [
    path('',views.MainView.as_view(),name="main"),
    path('search/',views.MainView.form,name="search"),
    path('results/',views.ResultView.show,name="result"),
    path('loading/',views.LoadingView.ajax_view,name="loading"),
]