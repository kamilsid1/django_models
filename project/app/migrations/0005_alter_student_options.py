# Generated by Django 5.0.3 on 2024-04-02 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_student_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['-Name'], 'verbose_name': 'stu'},
        ),
    ]
