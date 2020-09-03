import django
django.setup()
from Quiz.models import Question
from Quiz import randomNum
from django.shortcuts import render

def Questionlist(request):
    question = Question.objects.all()
    return render(request, 'Quiz_test.html', {'Questionlist':question})

def Quiz(request, generate_num):
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

def quizIntro(request):
    return render(request,"../templates/quiz-intro.html")

def getUserChoice(request):
    request.encoding = 'utf-8'

    #question object list
    question_list = Question.objects.all()

    #user answer list
    userChoiceList = []
    question_num = len(question_list)

    #dic for Questions and User Answers
    question_dic = {}
    if request.POST:
        for i in range(question_num):
            userChoice = request.POST.get(str(question_list[i].id))
            if userChoice == None:
                userChoice = 'You did not answer this question'
            userChoiceList.append(userChoice)
            question_dic[question_list[i]] = userChoice


    grade,score,suggestion = getScore(question_list, userChoiceList)
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
