# Generated by Django 4.2.7 on 2023-11-26 17:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student_app', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=200)),
                ('course_description', models.TextField(max_length=200)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher_app.teacher')),
                ('student', models.ManyToManyField(blank=True, to='student_app.student')),
            ],
        ),
        migrations.CreateModel(
            name='Assignmet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher_app.course')),
            ],
        ),
    ]
