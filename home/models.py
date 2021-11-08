import datetime
from django import template
from django.db import models
from django.utils import timezone
from django.views import generic
# from django.utils import timezone
# Create your models here.
class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(selft):
        return selft.pub_date>=timezone.now()- datetime.timedelta(days=1)
class Choice(models.Model):
    # question=models.ForeignKey(Question, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=100)
    votes=models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
# class IndexView(generic.ListView):
#     template_name='home/index1html'
#     context_object_name='lastest_question_list'
#     def get_Queryset(self):
#         return Question.objects.order_by('id')
# class DetaillView(generic.DetailView):
#     template_name='home/detail.html'
#     model=Question
# class ResultView(generic.DetailView):
#     model=Question
#     template_name='home/results.html'
# def vote(request, question_id):