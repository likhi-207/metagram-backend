# Generated by Django 5.2.4 on 2025-07-17 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='userName',
            new_name='username',
        ),
    ]
