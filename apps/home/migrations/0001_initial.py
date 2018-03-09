# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-01 13:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='文章标题')),
                ('content', models.TextField(verbose_name='文章内容')),
                ('created_time', models.DateTimeField(verbose_name='创建时间')),
                ('excerpt', models.TextField(blank=True, max_length=200, verbose_name='文章摘要')),
                ('author', models.CharField(max_length=100, verbose_name='作者')),
                ('views_num', models.PositiveIntegerField(default=0, verbose_name='阅读数量')),
            ],
            options={
                'ordering': ['-created_time'],
                'verbose_name_plural': '文章',
                'verbose_name': '文章',
            },
        ),
        migrations.CreateModel(
            name='ProgressBar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='进度条名称')),
                ('progress', models.IntegerField(verbose_name='进度条进程')),
                ('remarks', models.CharField(max_length=100, verbose_name='备注')),
            ],
            options={
                'verbose_name_plural': '进度条',
                'verbose_name': '进度条',
            },
        ),
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='捐助人')),
                ('money', models.IntegerField(verbose_name='捐助金额')),
                ('channel', models.IntegerField(choices=[(1, '微信'), (2, '支付宝')], verbose_name='捐助渠道')),
                ('date', models.DateField(verbose_name='捐助时间')),
                ('remarks', models.CharField(default='-', max_length=100, verbose_name='备注')),
            ],
            options={
                'verbose_name_plural': '捐助',
                'verbose_name': '捐助',
            },
        ),
    ]