# Generated by Django 5.0.3 on 2024-04-01 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Stu_Name', models.CharField(max_length=50)),
                ('Stu_Email', models.EmailField(max_length=254)),
                ('Stu_Contact', models.IntegerField()),
                ('Stu_Add', models.CharField(max_length=100)),
            ],
        ),
    ]
