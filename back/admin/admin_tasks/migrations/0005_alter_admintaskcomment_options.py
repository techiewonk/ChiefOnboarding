# Generated by Django 3.2.10 on 2022-01-11 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_tasks', '0004_auto_20211023_0206'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='admintaskcomment',
            options={'ordering': ['-date']},
        ),
    ]
