import random
import django
django.setup()
from Quiz.models import Question
from Quiz import randomNum
from django.shortcuts import render
from django.template import Context

def Questionlist(request):
    question = Question.objects.all()
    return render(request, 'Quiz_test.html', {'Questionlist':question})

def start_quiz(request):
    if 'start' in request.get:
        generate_num = randomNum.generateRandomNum()
        #Quiz(request, generate_num)
    return render(request, '../templates/base.html')

def Quiz(request, generate_num):
    view_name = "Quiz before submitted"
    quiz_question_numbers = len(generate_num)
    question_objects = []
    question_list = []
    ChoiceA_list = []
    ChoiceB_list = []
    ChoiceC_list = []
    q_dic = {}
    id_list = randomNum.generateRandomNum()
    for i in range(3):
        random_id = id_list[i]
        question = Question.objects.get(id=random_id)
        question_objects.append(question)
        q_dic[question.question] = [question.choiceA,question.choiceB,question.choiceC]
        question_list.append(question.question)
        ChoiceA_list.append(question.choiceA)
        ChoiceB_list.append(question.choiceB)
        ChoiceC_list.append(question.choiceC)

    return render(request, "../templates/Quiz_before.html", {'questionlist':question_objects}
    )

def done_question():
    #question = start_quiz(request)
    pass

def Home(request):
    view_name = "Quiz after submitted"
    return render(request, "../templates/index.html")