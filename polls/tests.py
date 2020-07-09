from django.test import TestCase,Client
from datetime import datetime
from django.utils import timezone
from django.urls import reverse
from .models import Question

# Create your tests here.
def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text,pub_date=time)

class QuestionIndeViewTests(TestCase):
    def test_no_questions(self):
        # 질문이 없으면 적절한 메세지를 보여준다
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'],[])

    def test_past_question(self):
        # 과거 질문들을 인덱스페이지에 질문과 함께 올린다
        create_question(question_text="Past question.",days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )


    def test_future_question_and_past_question(self):
        # 과거, 미래의 질문들일 있다면 과거만 보여준다
        create_question(question_text="Past question.",days=-30)
        create_question(question_text="Future qestion.",days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )
    
    def test_two_past_questions(self):
        # 질문인덱스페이지는 여러개 질문을 보여줄수잇다
        create_question(question_text="Past question 1.",days=-30)
        create_question(question_text="Past question 2.",days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question 2.>', '<Question: Past question 1.>']
        )

