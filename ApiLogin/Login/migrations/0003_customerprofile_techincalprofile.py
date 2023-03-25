# Generated by Django 3.1.2 on 2023-03-10 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0002_auto_20230310_1950'),
    ]

    operations = [
        migrations.CreateModel(
            name='TechincalProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identityimage', models.ImageField(blank=True, null=True, upload_to='pic')),
                ('name', models.CharField(max_length=200)),
                ('domin', models.CharField(max_length=200)),
                ('phonenumber', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=200)),
                ('techincal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Login.techincals')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companname', models.CharField(max_length=150)),
                ('manager', models.CharField(max_length=150)),
                ('technicalmanger', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=150)),
                ('phonenumber', models.CharField(max_length=150)),
                ('managermobile', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150)),
                ('website', models.CharField(max_length=150)),
                ('facebook', models.CharField(max_length=150)),
                ('serialnumber', models.CharField(max_length=150)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='pic')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Login.customers')),
            ],
        ),
    ]
