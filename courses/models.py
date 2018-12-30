from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Lesson(models.Model):
	CATEGORIES = ((1,'Mathematics'),
		(2,'Literature'),
		(3,'Science'),)
	LEVELS = ((1,'Introductory'),
		(2,'Basic'),
		(3,'Medium'),
		(4, 'Hard'),
		(5, 'Expert'))
	lesson_name = models.CharField(max_length = 200)
	lesson_category = models.IntegerField(choices=CATEGORIES)
	lesson_text = models.TextField()
	lesson_course = models.CharField(max_length=50)
	lesson_level = models.IntegerField(choices = LEVELS)
	lesson_image = models.ImageField(blank=True)
	pub_date = models.DateTimeField()
	lesson_abstract = models.CharField(max_length = 400)
	lesson_author = models.CharField(max_length = 100)


	def __str__(self):
		return self.lesson_name

class UserCard(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	lesson = models.ForeignKey(Lesson, on_delete = models.CASCADE)
	quiz_complete = models.BooleanField()
	score = models.FloatField(default = None)

	def __str__(self):
		return self.user.username + " " + self.lesson.lesson_name

class Question(models.Model):
	lesson = models.ForeignKey(Lesson, on_delete = models.CASCADE)
	question_text = models.TextField()

	def __str__(self):
		return "Lesson: " + self.lesson.lesson_name + "   Question: " + self.question_text

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete = models.CASCADE)
	choice_text = models.TextField()
	correct = models.BooleanField()

	def __str__(self):
		return "Lesson: " + self.question.lesson.lesson_name + "   Question: " + self.question.question_text + "   Choice: " + self.choice_text + "   Is correct? " + str(self.correct)