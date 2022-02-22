import datetime
from django.contrib import admin
from django.db import models
from django.utils import timezone

# REFERENCES
# Title: Writing your first Django app, part 2
# Author: Django Software Foundation and individual contributors
# Date: 2022
# Code version: 3.2
# URL: https://docs.djangoproject.com/en/3.2/intro/tutorial02/
# Software License: <license software is released under>

# Note the addition of import datetime and from django.utils import timezone,
# to reference Python’s standard datetime module
# and Django’s time-zone-related utilities in django.utils.timezone, respectively.


class Question(models.Model):
    question_text = models.CharField(max_length=200)  # creates a field of text in database
    pub_date = models.DateTimeField('date published')  # stores datetime object

    def __str__(self):
        return self.question_text

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    #  A foreign key with cascade delete means that
    #  if a record in the parent table is deleted, then the corresponding records
    #  in the child table will automatically be deleted.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # many-to-one relationship (Choice -> Question)
    choice_text = models.CharField(max_length=200)  # creates a field in database
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


# from Django tutorial
class Deepthought(models.Model):
    thought_text = models.CharField(max_length=200)

    def __str__(self):
        return self.thought_text
