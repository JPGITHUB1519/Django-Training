from django.contrib import admin
from .models import Question, Choice
# Register your models here.

# to add choice options from Question
class ChoiceInline(admin.TabularInline):
	model = Choice
	Extra = 3

# modifying admin
class QuestionAdmin(admin.ModelAdmin):
	# fielsets - > divide the form in sections
	fieldsets = [
		(None, {'fields': ['question_text']}),
		('Date information' , {'fields': ["pub_date"],
		# collapse
		'classes' : ['collapse']})
	]
	# adding Choices to Questions
	inlines = [ChoiceInline]
	# changing the Select question to change fields
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	# adds a "Filter" sidebar that lets people filter the change 
	# list by the pub_date field:
	list_filter = ['pub_date']
	# search capability filted by question_text
	search_fields = ['question_text']


# register to the admin
admin.site.register(Question, QuestionAdmin)