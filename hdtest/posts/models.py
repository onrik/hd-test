# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Автор')
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    tags = TaggableManager(verbose_name='Теги')

    class Meta:
        ordering = ('-create_date',)
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', verbose_name='Пост')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, verbose_name='Автор')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    text = models.TextField(verbose_name='Текст')

    class Meta:
        ordering = ('-create_date',)
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
