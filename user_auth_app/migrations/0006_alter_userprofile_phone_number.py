# Generated by Django 5.1.4 on 2024-12-16 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth_app', '0005_alter_userprofile_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(blank=True, default='', help_text="Telephone number in the format: '999999999'. Up to 15 digits allowed.", max_length=15),
            preserve_default=False,
        ),
    ]
