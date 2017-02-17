from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from .models import Question, Choice

"""
Generic View Explanation
Detail View -> traer un objeto de la base de datos (DetailVew), 
ListView - > Lista de Objetos
(CreateView, UpdateView y DeleteView) -> para crear, actualizar o borrar 
"""

# Create your views here.
class IndexView(generic.ListView):
	""" ListView view to representing a list of objects."""
	template_name = 'polls/index.html'
	# changing template context model name
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		"""Return the last five published questions."""
		return Question.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
	""" Use detail View para obtener un solo objeto de l bd
		needs the primary key to find the right object to display
	"""
	""" View to show the Questions Data filter by the pk """
	model = Question
	template_name = 'polls/detail.html'
	# using the default ContextName question

class ResultsView(generic.DetailView):
	""" View to show the results vote from a Question"""
	model = Question
	template_name = 'polls/results.html'

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
