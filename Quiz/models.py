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
    questionId = models.IntegerField()
    category = models.CharField(max_length=10)
    keyword = models.CharField(max_length=100)
    imageurl = models.CharField(max_length=100)

class Category(models.Model):

    title = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    category = models.CharField(max_length=10)






