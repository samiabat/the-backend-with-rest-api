# Generated by Django 4.0.1 on 2022-01-24 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MealSystem', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Admin',
        ),
        migrations.RemoveField(
            model_name='student',
            name='groups',
        ),
    ]
