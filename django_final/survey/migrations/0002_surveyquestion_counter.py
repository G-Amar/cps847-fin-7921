# Generated by Django 4.1.7 on 2023-04-18 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveyquestion',
            name='counter',
            field=models.IntegerField(default=5),
        ),
    ]
