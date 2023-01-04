from django.db import models

# Create your models here.
class Question(models.Model):
    subject = models.CharField(max_length=200, verbose_name='질문 제목')
    content = models.TextField(verbose_name='질문 내용')
    create_date = models.DateTimeField(verbose_name='질문 생성 일시')

    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField(verbose_name='답변 내용')
    create_date = models.DateTimeField(verbose_name='답변 생성 일시')