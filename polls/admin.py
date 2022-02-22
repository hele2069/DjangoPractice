from django.contrib import admin
from .models import Question, Choice, Deepthought

# REFERENCES
# Title: Writing your first Django app, part 2
# Author: Django Software Foundation and individual contributors
# Date: 2022
# Code version: 3.2
# URL: https://docs.djangoproject.com/en/3.2/intro/tutorial02/
# Software License: <license software is released under>


class ChoiceInLine(admin.TabularInline):  # vs. StackedInline
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInLine]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']  # filter sidebar that lets people filter the change list by the pub_date field:
    search_fields = ['question_text']  # search bar


# from Django tutorial
class DeepthoughtAdmin(admin.ModelAdmin):
    model = Deepthought


admin.site.register(Question, QuestionAdmin)
admin.site.register(Deepthought, DeepthoughtAdmin)
