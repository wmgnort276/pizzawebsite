from django.http.request import HttpRequest
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from .models import Choice, Question
from django.views import generic
# Create your views here.
def index(request):
    response = HttpResponse()
    response.writelines("<h1>Xin chao</h1>")
    response.write("Day la apphome")
    return response
def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except:
    #     raise Http404("Question does no exist")
    # return render(request, 'home/detail.html', {'question': question})
    # return HttpResponse("You're looking at question %s." % question_id)
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'home/detail.html',{'question': question})
def results(request, question_id):
    response= HttpResponse("You're looking at the results of the question %s.")
    return HttpResponse(response % question_id)
def vote(request, question_id):
    # return HttpResponse("You're looking at the votes of the quetion %s." %question_id)
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request,'home/detail.html',{
        'question':question,
        'error_message':"You didn't select a choice.",})
    else:
        selected_choice.votes+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('home:results',args=(question.id,)))
def index1(request):
    lastest_question_list = Question.objects.order_by('id')
    template = loader.get_template('home/pagas.html')
    context={'lastest_question_list': lastest_question_list}
    return HttpResponse(template.render(context,request))
class IndexView(generic.ListView):
    template_name='home/pagas.html'
    context_object_name='lastest_question_list'
    def get_queryset(self):
        return Question.objects.order_by('id')
class DetailView(generic.DetailView):
    model = Question
    template_name='home/detail.html'
class ResultView(generic.DetailView):
    model=Question
    template_name='home/results.html'

    


