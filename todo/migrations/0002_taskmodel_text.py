# Generated by Django 3.1 on 2020-08-24 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='text',
            field=models.TextField(default=1, verbose_name='Task'),
            preserve_default=False,
        ),
    ]
