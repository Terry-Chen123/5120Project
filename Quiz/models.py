from django.db import models

class Question(models.Model):

    question = models.CharField(max_length=1000)
    choiceA = models.CharField(max_length=500)
    choiceB = models.CharField(max_length=500)
    choiceC = models.CharField(max_length=500)
    answer = models.CharField(max_length=32)
    feedbackA = models.CharField(max_length=500)
    feedbackB = models.CharField(max_length=500)
    feedbackC = models.CharField(max_length=500)
    suggestion = models.CharField(max_length=500)

class Quiz(models.Model):

    feedback = models.CharField(max_length=1000)
    grade = models.IntegerField()

class Quiz_Question(models.Model):

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    correctOrNot = models.BooleanField()
    userChoice = models.CharField(max_length=10)





