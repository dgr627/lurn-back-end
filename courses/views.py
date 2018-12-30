from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404, render, redirect

from rest_framework.decorators import *

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework import authentication, permissions

import ujson

from .serializers import *

def start(request):
	return render(request, 'courses/start.html')


def index(request):
    lesson_list = Lesson.objects.order_by('-pub_date')
    completed_lessons=[]
    incomplete_lessons=[]
    user=request.user
    user_cards = UserCard.objects.filter(user=user)
    for x in lesson_list:
    	count = 0
    	for y in user_cards:
    		if x.lesson_name == y.lesson.lesson_name:
    			completed_lessons.append(x)
    			count=1
    	if count == 0:
    		incomplete_lessons.append(x)
    context = {'username': user.get_username(), 
    'completed_lessons': completed_lessons,
    'incomplete_lessons': incomplete_lessons}
    return render(request, 'courses/index.html', context)

def login_page(request):
	logout(request)
	return render(request, 'courses/login.html')

def create_page(request):
	logout(request)
	return render(request, 'courses/create.html')

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def login_api(request):
	data=ujson.loads(request.body)
	print(data)
	username = data["username"]
	password = data["password"]
	user = authenticate(username=username, password=password)
	if user is not None:
		token =Token.objects.get(user=user)
		return Response({'success': True, 'token': token.key})
	else:
		return HttpResponse("Invalid Login")

def login_action(request):
	username = request.POST.get("username")
	password = request.POST.get("password")
	user = authenticate(username=username, password=password)
	if user is not None:
		login(request, user)
		return index(request)
	else:
		return HttpResponse("Invalid Login")

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def create_action(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	if User.objects.filter(username=username).exists():
		return HttpResponse("Username Taken")
	else:
		user = User.objects.create_user(username = username, password = password)
		user.save()
		token = Token.objects.create(user=user)
		token.save()
		login(request, user)
		return index(request)

@login_required(login_url = '/courses/login')
def display_lesson(request, lesson_id):
	lesson = get_object_or_404(Lesson, pk=lesson_id)
	user = request.user
	if not UserCard.objects.filter(user = user, lesson = lesson):
		card = UserCard(user = request.user, lesson = lesson, score = 0, quiz_complete = False)
		card.save()
	else:
		card = UserCard.objects.filter(user = user, lesson = lesson)[0]

	questions = Question.objects.filter(lesson = lesson)
	choices=[]
	for question in questions:
		choices.append(Choice.objects.filter(question = question))

	context = {'lesson' : lesson,
	'user' : user,
	'card' : card,
	'questions' : questions,
	'choices' : choices,}
	return render(request, 'courses/lesson_content.html', context)

def display_quiz(request, lesson_id):
	lesson = get_object_or_404(Lesson, pk=lesson_id)
	user = request.user
	if not UserCard.objects.filter(user = user, lesson = lesson):
		card = UserCard(user = request.user, lesson = lesson, score = 0, quiz_complete = False)
		card.save()
	else:
		card = UserCard.objects.filter(user = user, lesson = lesson)[0]

	questions = Question.objects.filter(lesson = lesson)
	choices=[]
	for question in questions:
		choices.append(Choice.objects.filter(question = question))

	context = {'lesson' : lesson,
	'user' : user,
	'card' : card,
	'questions' : questions,
	'choices' : choices,
	'complete': card.quiz_complete,}
	return render(request, 'courses/display_quiz.html', context)

def submit_quiz(request, lesson_id):
	lesson = get_object_or_404(Lesson, pk=lesson_id)
	user = request.user
	if not UserCard.objects.filter(user = user, lesson = lesson):
		card = UserCard(user = request.user, lesson = lesson, score = 0, quiz_complete = False)
		card.save()
	else:
		card = UserCard.objects.filter(user = user, lesson = lesson)[0]
	x = request.POST
	correct = 0 
	incorrect = 0
	for key in x:
		try:
			choice = Choice.objects.get(pk = x[key])
		except:
			continue
		print(choice.correct)
		if choice:
			if choice.correct == True:
				correct = correct +1
			else:
				incorrect = incorrect+1
	print(correct)
	average = correct/(correct+incorrect)
	card.score = average
	card.quiz_complete=True
	card.save()
	return HttpResponse("Done")


def sign_out(request):
	logout(request)
	return start(request)



