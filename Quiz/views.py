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

def home(request):
    return render(request, "../templates/index.html")

def service(request):
    return render(request, "../templates/service.html")

def readMore(request):
    return render(request,"../templates/read-more.html")

def evaluation(request):
    question = Question.objects.all()
    return render(request, '../templates/evaluation.html', {'Questionlist': question})

def review(request):
    return render(request,"../templates/review.html")

def getUserChoice(request):
    request.encoding = 'utf-8'
    #question object list
    question_list = Question.objects.all()
    #user answer list
    userChoiceList = []
    num_list = []
    question_num = len(question_list)
    #dic for Questions and User Answers
    question_dic = {}
    if request.POST:
        for i in range(question_num):
            userChoice = request.POST.get(str(question_list[i].id))
            userChoiceList.append(userChoice)
            question_dic[question_list[i]] = userChoice

    grade,score = getScore(question_list, userChoiceList)
    return render(request, '../templates/review.html', {'userChoice':userChoiceList,
                                                        'question_dic':question_dic,
                                                        'grade':grade,
                                                        'score':score})

def getScore(Q_list, Ans_list):
    score = 0
    total_score = 10 *len(Q_list)
    for i in range(len(Q_list)):
        if Q_list[i].answer == Ans_list[i]:
            score += 10
    result = ""
    if score / total_score < 0.3:
        result = "D"
    elif 0.3 <= score / total_score < 0.5:
        result = "C"
    elif 0.5 <= score / total_score < 0.8:
        result = "B"
    elif 0.8 <= score / total_score:
        result = "A"
    final_score = str(score) + "/" + str(total_score)
    return result, final_score
