from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Question, Choice

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """ Return the last five published questions. """
        return Question.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results/html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question":question,
                "error_message":"You didn't select a choice",
            },
        )
    else:
        # POST 데이터를 성공적으로 처리하면 반드시 HttpResponseRedirect 반환
        # 뒤로가기 버튼을 눌러도 데이터가 2번 표현되는거 방지 가능
        selected_choice.votes +=1
        selected_choice.save()

        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
    
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)

#     return render(request, "polls/results.html", {"question": question})