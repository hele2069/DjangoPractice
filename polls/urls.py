from django.urls import path
from . import views

# REFERENCES
# Title: Writing your first Django app, part 2
# Author: Django Software Foundation and individual contributors
# Date: 2022
# Code version: 3.2
# URL: https://docs.djangoproject.com/en/3.2/intro/tutorial02/
# Software License: <license software is released under>


app_name = 'polls'
# url patterns for 'submit' and 'thoughts' are from Django tutorial
urlpatterns = [
    # ex: /polls/
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    # ex: /polls/deepthoughts
    path('deepthoughts/', views.submit_thoughts.as_view(), name='submit'),
    # ex: /polls/deepthoughts/list
    path('deepthoughts/list/', views.thoughtsList.as_view(), name='thoughts')
]