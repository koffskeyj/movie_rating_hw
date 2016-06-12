# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-11 13:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_title', models.CharField(max_length=50)),
                ('release_date', models.CharField(max_length=12)),
                ('video_release_date', models.CharField(default='', max_length=12)),
                ('URL', models.CharField(max_length=300)),
                ('unknown', models.IntegerField()),
                ('Action', models.IntegerField()),
                ('Adventure', models.IntegerField()),
                ('Animation', models.IntegerField()),
                ('Childrens', models.IntegerField()),
                ('Comedy', models.IntegerField()),
                ('Crime', models.IntegerField()),
                ('Documentary', models.IntegerField()),
                ('Drama', models.IntegerField()),
                ('Fantasy', models.IntegerField()),
                ('Film_Noir', models.IntegerField()),
                ('Horror', models.IntegerField()),
                ('Musical', models.IntegerField()),
                ('Mystery', models.IntegerField()),
                ('Romance', models.IntegerField()),
                ('Sci_Fi', models.IntegerField()),
                ('Thriller', models.IntegerField()),
                ('War', models.IntegerField()),
                ('Western', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Rater',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=1, null=True)),
                ('occupation', models.CharField(max_length=30)),
                ('zipcode', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('time_stamp', models.IntegerField()),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movierating.Movie')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movierating.Rater')),
            ],
        ),
    ]
