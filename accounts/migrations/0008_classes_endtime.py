# Generated by Django 4.2.5 on 2023-12-01 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_classes_starttime_course_coursename'),
    ]

    operations = [
        migrations.AddField(
            model_name='classes',
            name='endtime',
            field=models.DateField(null=True),
        ),
    ]
