from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse, Http404
from django.contrib import messages

from .models import Question, Choice


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
    # detail.html 파일을 약간 수정해서 result.html을 만들고
    # 질문에 대한 모든 선택사항의 선택수(votes)를 출력
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question,
    }
    return render(request, 'polls/results.html', context)


def vote(request, question_id):
    # request 의 method 가 POST 방식일때
    # 전달받은 데이터중 'choice'키에 해당하는 값을
    # HttpResponse에 적절히 돌려준다.
    if request.method == 'POST':
        data = request.POST
        try:
            choice_id = data['choice']
            choice = Choice.objects.get(id=choice_id)
            choice.votes += 1
            choice.save()
            return redirect('polls:results', question_id)
        except(KeyError, Choice.DoesNotExist):
            messages.add_message(
                request,
                messages.ERROR,
                "You didn't select a choice",
            )
        # choice키에 해당하는 Choice인스턴스의 vote 값을 1 증가시키고
        # 데이터베이스에 변경사항을 반영
        # 이후 results페이지로 redirect

        return redirect('polls:results', question_id)
    else:
        return HttpResponse("You're voting on question %s." % question_id)


