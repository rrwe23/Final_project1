from django.db import models
from django.conf import settings



class Question(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    content = models.TextField()
    answers = models.OneToOneField('products.Answer', on_delete = models.CASCADE)

class Answer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    content = models.TextField()
    questions = models.OneToOneField('products.Question', on_delete = models.CASCADE)
