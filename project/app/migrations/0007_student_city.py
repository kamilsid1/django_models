# Generated by Django 5.0.3 on 2024-04-02 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_student_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='City',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
