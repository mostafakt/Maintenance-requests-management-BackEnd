# Generated by Django 3.1.2 on 2023-03-15 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0007_auto_20230315_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerprofile',
            name='customer',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='Login.customers'),
        ),
        migrations.AlterField(
            model_name='techincalprofile',
            name='techincal',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='Login.techincals'),
        ),
    ]
