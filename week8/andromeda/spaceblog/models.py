# coding: utf-8

from __future__ import unicode_literals

from django.db import models

class Post(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    text = models.TextField('Текст')
    create_date = models.DateTimeField('Дата создание')
    
    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
    
    def __unicode__(self):          # для Python 2.x unicode
                                    # для Py 3.x  __str__
        return '{0} {1}'.format(self.title, self.create_date)
        
        
    
    
