from django.db import models


class Users(models.Model):
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    login = models.CharField('Логин', max_length=50)
    password = models.CharField('Пароль', max_length=50)

    def __str__(self):
        return self.first_name
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class Courses(models.Model):
    title = models.CharField('Название курса', max_length=100)
    description = models.TextField(verbose_name='описание')
    #teacher = models.ForeignKey(Users, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Преподаватель')
    date = models.DateTimeField('Дата начала')
    price = models.IntegerField(verbose_name='Цена')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
    

