# Generated by Django 4.2.6 on 2023-11-04 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_user_roleid'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Role',
        ),
        migrations.AddField(
            model_name='user',
            name='roleID',
            field=models.IntegerField(choices=[(1, 'Student'), (2, 'Teacher'), (3, 'Administrator')], default=1),
        ),
    ]
