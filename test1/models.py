from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")

    def __str__(self):
        return f'id:{self.id} {self.title}'

class Comment(models.Model):
    author = models.CharField(max_length=50, verbose_name="Автор")
    desc = models.TextField(max_length=500, verbose_name='Коммент')


    def __str__(self):
        return f'ID:{self.id}, Author: {self.author.capitalize()}'
