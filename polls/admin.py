from django.contrib import admin

from .models import Question, Choice, Deepthought


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


class DeepthoughtAdmin(admin.ModelAdmin):
    model = Deepthought


admin.site.register(Question, QuestionAdmin)
admin.site.register(Deepthought, DeepthoughtAdmin)
