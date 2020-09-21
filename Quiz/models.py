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
    #image = models.ImageField()

class Quiz(models.Model):

    feedback = models.CharField(max_length=1000)
    grade = models.IntegerField()

class Quiz_Question(models.Model):

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    correctOrNot = models.BooleanField()
    userChoice = models.CharField(max_length=10)

class Category(models.Model):

    title = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    category = models.CharField(max_length=10)

class Hospital1(models.Model):

    longitude = models.DecimalField(max_digits=13, decimal_places=10)
    latitude = models.DecimalField(max_digits=13, decimal_places=10)
    hospital_name = models.CharField(max_length=500)
    hospital_type = models.CharField(max_length=500)
    streetNum = models.IntegerField()
    roadName = models.CharField(max_length=500)
    roadType = models.CharField(max_length=500)
    area = models.CharField(max_length=500)
    postcode = models.IntegerField()
    state = models.CharField(max_length=500)
    phone = models.CharField(max_length=100)
    website = models.CharField(max_length=500)

class Clinic(models.Model):

    clinic_name = models.CharField(max_length=500)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    longitude = models.DecimalField(max_digits=13, decimal_places=10)
    latitude = models.DecimalField(max_digits=13, decimal_places=10)
    clinic_type = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    suburb = models.CharField(max_length=500)
    phone = models.CharField(max_length=20)
    website = models.CharField(max_length=500)




