from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader
from django.http import Http404
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {'latest_question_list':latest_question_list,}
#     return HttpResponse(template.render(context,request))

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list':latest_question_list,}
    return render(request,'polls/index.html',context)

def detail(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html',{'question':question})
    # return HttpResponse("질문을 보고 있다 %s." % question_id)

def results(request,question_id):
    response = "너는 질문의 결과를 보고 있다. %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("질문에 투표하고 있다 %s." % question_id)

