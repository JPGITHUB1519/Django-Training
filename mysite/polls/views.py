from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Question

# Create your views here.

def index(request):
	# gettip top 5 lattest post
	latest_question_list = Question.objects.order_by("-pub_date")[:5]
	#output = ", ".join([q.question_text for q in latest_question_list])
	# render template
	context = {
		"latest_question_list" : latest_question_list,
	}
	return render(request, 'polls/index.html', context)

def detail(request, question_id):
	# long form
	# try:
	# 	question = Question.objects.get(pk=question_id)
	# except Question.DoesNotExits:
	# 	# 404 Error
	# 	raise Http404("Question does not exit")

	# 404 shorcut if the record was not found
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
	response = "You're Looking at the results of the Question %s"
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You are voting on question %s" % question_id)
