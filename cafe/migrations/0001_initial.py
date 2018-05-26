# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-26 06:38
from __future__ import unicode_literals

import cafe.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('name', models.CharField(blank=True, max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to=cafe.models.get_file_path)),
                ('taking_time', models.IntegerField(default=0)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cafe.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('comment', models.CharField(blank=True, max_length=50)),
                ('state', models.IntegerField(default=0)),
                ('taking_time', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnt', models.PositiveIntegerField()),
                ('menu_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cafe.Menu')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cafe.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(blank=True, max_length=20)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to=cafe.models.get_file_path)),
                ('type', models.IntegerField(default=0)),
                ('point', models.IntegerField(default=0)),
                ('comment', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WatingTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cafe.Profile'),
        ),
    ]
