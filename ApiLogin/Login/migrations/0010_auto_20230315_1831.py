# Generated by Django 3.1.2 on 2023-03-15 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0009_auto_20230315_1813'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='techincal',
        ),
        migrations.AddField(
            model_name='orders',
            name='techincal',
            field=models.ManyToManyField(default=None, to='Login.TechincalProfile'),
        ),
    ]
