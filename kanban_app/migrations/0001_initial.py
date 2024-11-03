# Generated by Django 5.1.2 on 2024-11-03 16:02

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('technical_task', 'Technical Task'), ('user_story', 'User Story')], max_length=20)),
                ('due_date', models.DateField()),
                ('priority', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('urgent', 'Urgent')], max_length=20)),
                ('status', models.CharField(choices=[('todo', 'Todo'), ('in_progress', 'In progress'), ('await_feedback', 'Await feedback'), ('done', 'Done')], max_length=20)),
                ('position', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(help_text="Telephone number in the format: '+999999999'. Up to 15 digits allowed.", max_length=15, validators=[django.core.validators.RegexValidator('^\\+?1?\\d{9,15}$')])),
                ('user_color', models.CharField(max_length=7)),
                ('type', models.CharField(choices=[('user_from_signup', 'User from signup'), ('user_from_contacts', 'User from contacts')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Subtask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('is_completed', models.BooleanField(default=False)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtasks', to='kanban_app.task')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='users',
            field=models.ManyToManyField(related_name='tasks', to='kanban_app.user'),
        ),
    ]
