from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from .models import Choice, Question, Deepthought

# REFERENCES
# Title: Writing your first Django app, part 2
# Author: Django Software Foundation and individual contributors
# Date: 2022
# Code version: 3.2
# URL: https://docs.djangoproject.com/en/3.2/intro/tutorial02/
# Software License: <license software is released under>
#
# Title: Django - Generic editing views
# Date: 2022
# Code Version: 4.0
# URL: https://docs.djangoproject.com/en/4.0/ref/class-based-views/generic-editing/
# Software License: <>


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


# from Django's documentations on generic views
class submit_thoughts(generic.CreateView):
    template_name = 'polls/submit.html'
    model = Deepthought
    fields = ['thought_text']

    def get_success_url(self):
        return reverse('polls:thoughts')


# from Django tutorial
class thoughtsList(generic.ListView):
    template_name = 'polls/thoughts.html'
    context_object_name = 'thought_list'

    def get_queryset(self):
        return Deepthought.objects.all()
