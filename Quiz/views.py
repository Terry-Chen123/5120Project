import django
django.setup()
from Quiz.models import Question,Category
from Quiz import randomNum
from django.shortcuts import render



def home(request):
    return render(request, "../templates/index.html")

def readMore(request):
    return render(request,"../templates/read_more.html")

def service(request):
    return render(request, "../templates/service.html")

def quizCategory(request):
    categoryA = Category.objects.all()[0]
    categoryB = Category.objects.all()[1]
    categoryC = Category.objects.all()[2]
    return render(request,'../templates/quiz_category.html',{'categoryA':categoryA,
                                                             'categoryB':categoryB,
                                                             'categoryC':categoryC})

def quizIntro(request):
    categoryA = Category.objects.all()[0]
    categoryB = Category.objects.all()[1]
    categoryC = Category.objects.all()[2]

    if request.POST:
        if 'A' in request.POST:
            category = categoryA
        elif 'B' in request.POST:
            category = categoryB
        elif 'C' in request.POST:
            category = categoryC

    return render(request,"../templates/quiz_intro.html",{'category':category})

def evaluation(request):
    question = []
    questionA = Question.objects.all()[0:5]
    questionB = Question.objects.all()[5:10]
    questionC = Question.objects.all()[10:15]
    if request.POST:
        if 'A' in request.POST:
            question = questionA
        elif 'B' in request.POST:
            question = questionB
        elif 'C' in request.POST:
            question = questionC
    return render(request, '../templates/evaluation.html', {'Question': question,})


def getUserChoice(request):
    request.encoding = 'utf-8'

    #question object list
    question_list = Question.objects.all()
    question = []

    #user answer list
    userChoiceList = []
    question_num = len(question_list)

    #dic for Questions and User Answers
    question_dic = {}
    if request.POST:
        if 'A' in request.POST:
            question = question_list[0:5]
        elif 'B' in request.POST:
            question = question_list[5:10]
        elif 'C' in request.POST:
            question = question_list[10:15]
        for i in range(5):
            userChoice = request.POST.get(str(question[i].id))
            if userChoice == None:
                userChoice = 'You did not answer this question'
            userChoiceList.append(userChoice)
            question_dic[question[i]] = userChoice

    grade,score,suggestion = getScore(question, userChoiceList)
    return render(request, '../templates/review.html', {'userChoice':userChoiceList,
                                                        'question_dic':question_dic,
                                                        'grade':grade,
                                                        'score':score,
                                                        'suggestion':suggestion})

def getScore(Q_list, Ans_list):
    score = 0
    total_score = len(Q_list)
    for i in range(len(Q_list)):
        if Q_list[i].answer == Ans_list[i]:
            score += 1
    result = ""
    suggestion = ""
    if score  <= 2:
        result = "Woooooo!"
        suggestion = "Not so good, but no need to be panic and so long as you read through our website " \
                     "content about children's pneumonia, you will become a master on how to deal with " \
                     "the pneumonia emergency that happened to your child. Please click on this link " \
                     "to learn more about child pneumonia."
    elif 3 <= score  <+ 4:
        result = "Keep Learing!"
        suggestion = "You are doing good and almost master the knowledge of children's pneumonia, " \
                     "but still misunderstanding a little bit. If you want to get a full mark, " \
                     "feel free to go back and read the information, and do the quiz again. "
    elif  score == 5:
        result = "Excellent!"
        suggestion = "You got all of the right answers, but don’t be so proud and you may also need to learn " \
                     "some of the knowledge gap of children’s pneumonia."

    final_score = str(score) + "/" + str(total_score)
    return result, final_score, suggestion



