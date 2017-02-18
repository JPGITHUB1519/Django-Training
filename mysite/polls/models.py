from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
import datetime
# Create your models here.

# models
@python_2_unicode_compatible # support for python 2
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	# human readable name
	pub_date = models.DateTimeField('date published')

	# to printing beautiful in console
	def __str__(self):
		return self.question_text

	# custom method reutrn false / true
	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now

@python_2_unicode_compatible # support for python 2
class Choice(models.Model):
	# foreign key
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	# default = 0
	votes = models.IntegerField(default=0)

	# to printing beautiful in console
	def __str__(self):
		return self.choice_text
