# Generated by Django 5.1.2 on 2024-10-27 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kanban_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='assigned_to',
            new_name='assignedTo',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='due_date',
            new_name='dueDate',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='firebase_id',
            new_name='firebaseId',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='sub_tasks',
            new_name='subTasks',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='sub_tasks_completed',
            new_name='subTasksCompleted',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='task_column_order',
            new_name='taskColumnOrder',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='task_status',
            new_name='taskStatus',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='color',
            new_name='firebaseId',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='email_address',
            new_name='userColor',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='firebase_id',
            new_name='userEmailAddress',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='firstname',
            new_name='userFirstName',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='initials',
            new_name='userInitials',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='userName',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='phone_numer',
            new_name='userPhoneNumber',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='surname',
            new_name='userSurName',
        ),
    ]
