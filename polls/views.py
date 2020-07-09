# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Question
# from django.template import loader
# from django.http import Http404
# # def index(request):
# #     latest_question_list = Question.objects.order_by('-pub_date')[:5]
# #     template = loader.get_template('polls/index.html')
# #     context = {'latest_question_list':latest_question_list,}
# #     return HttpResponse(template.render(context,request))

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list':latest_question_list,}
#     return render(request,'polls/index.html',context)

# def detail(request,question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html',{'question':question})
#     # return HttpResponse("질문을 보고 있다 %s." % question_id)

# def results(request,question_id):
#     response = "너는 질문의 결과를 보고 있다. %s."
#     return HttpResponse(response % question_id)

# # def vote(request, question_id):
# #     return HttpResponse("질문에 투표하고 있다 %s." % question_id)

# from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import get_object_or_404, render
# from django.urls import reverse

# def vote(request, question_id):
#     question = get_object_or_404(Question,pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         return render(request, 'polls/detail.html',{'question':question,
#         'error_message': "선택을 안했어",})
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))


# def results(request,question_id):
#     question = get_object_or_404(Question,pk=question_id)
#     return render(request, 'polls/results.html', {'question':question})


# 클래스 뷰로 재정의

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DeleteView):
    model = Question
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',{'question':question,
        'error_message': "선택을 안했어",})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))