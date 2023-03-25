# Generated by Django 3.1.2 on 2023-03-15 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0005_auto_20230315_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='mancontact',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
        migrations.AddField(
            model_name='mancontact',
            name='name',
            field=models.CharField(default=None, max_length=150),
        ),
        migrations.AddField(
            model_name='mancontact',
            name='postion',
            field=models.CharField(default=None, max_length=150),
        ),
        migrations.AddField(
            model_name='mancontact',
            name='techincal',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Login.techincalprofile'),
        ),
        migrations.AddField(
            model_name='mancontact',
            name='telephone',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='orders',
            name='Frequencyofoccurane',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='orders',
            name='RequriedVisit',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='orders',
            name='location',
            field=models.CharField(default=None, max_length=150),
        ),
        migrations.AddField(
            model_name='orders',
            name='mancontact',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Login.mancontact'),
        ),
        migrations.AddField(
            model_name='orders',
            name='ordernumber',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='orders',
            name='timeofoccurrance',
            field=models.DateTimeField(default=None),
        ),
    ]