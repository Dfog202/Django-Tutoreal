from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # latest_question_list라는 키로 위 쿼리셋을 전달
    # polls/index.html을 이용해 render 결과를 리턴
    latest_question_list = get_list_or_404(
        Question.objects.order_by('-pub_date')[:5]
    )
    context = {
        'latest_question_list': latest_question_list,
    }
    # Template Does Not Exist
    # settings.py에서
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # question_id가 pk인 Question객체를 가저와서
    # context라는 이름을 가진 dict에 question이라는 키값으로 위 변수를 할당
    # 이후 polls/detail.html 과 context를 랜더한 결과를 리턴
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist as e:
    #     raise Http404('Question does not exist')

    # question.choice_set.
    # Choice.objects.filter(question=question).
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question,
    }
    # polls/detail에서 해당 question의 question_text를 출력
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    response = "You're looking at the result of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're votiong on question %s." % question_id)
