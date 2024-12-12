# Generated by Django 5.1.2 on 2024-12-10 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanban_app', '0007_alter_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='position',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
    ]