from django.db import models

class python(models.Model):
    question=models.CharField(max_length=200)
    answer=models.CharField(max_length=200)

    def __str__(self):
        return self.question

class html(models.Model):
    question=models.CharField(max_length=200)
    answer=models.CharField(max_length=200)
    
    def __str__(self):
            return self.question
class css(models.Model):
    question=models.CharField(max_length=200)
    answer=models.CharField(max_length=200)
    
    def __str__(self):
            return self.question
class javascript(models.Model):
    question=models.CharField(max_length=200)
    answer=models.CharField(max_length=200)
    
    def __str__(self):
            return self.question



