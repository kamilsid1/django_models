# Generated by Django 5.0.3 on 2024-04-02 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_stu_add_student_add_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['Name']},
        ),
    ]
