from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from samplesite.polls import Question, Choice


# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}

    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    return HttpResponse("")


def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choise_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExists):
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "you didnt select a choice."
        })
    else:
        selected_choice.vote += 1
        selected_choice.save()
        return HttpResponse(reverse('polls:result', args=(p.id,)))

