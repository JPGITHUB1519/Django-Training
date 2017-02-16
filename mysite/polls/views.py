from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Question, Choice

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
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html', {'question' : question})

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		# getting the value on the request post Dictionary
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	# key error if does not found in the request dictionary
	except(KeyError, Choice.DoesNotExist):
		# redisplay the question voting form
		return render(request, 'polls/detail.html', {
				'question' : question,
				'error_message' : "You didn't select a choice"
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.

	    # reverse is to generate the url like /polls/
	    # always generate HttpResponseRedirect after post
	    # This tip isn't specific to Django; it's just good Web development practice.
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
