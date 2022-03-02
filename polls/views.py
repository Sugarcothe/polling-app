from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse

from .models import Question, Choice

# Get questions and dipplay them

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request,  'polls/index.html', context)

# show specific questions and choices
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoestNoExist:
        raise Http404('QUESTION DOES NOT EXIST')
    return render(request, 'polls/detail.html', {'question': question})

# Get questions and display results
def results(request, question_id): 
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question })

# Vote for a question choice
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # print(request.POST['choice'])
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question form.
        return render(request, 'polls/details.html', {
            'question': question,
            'error_message' : "you didnt select a choice"
        })
    else: 
        selected_choice.votes += 1
        selected_choice.save()
        # always return an httpresponseredirect after succesfully dealing
        # with POST data. this prevents data from being posted twice if a 
        # user hits the back button
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))