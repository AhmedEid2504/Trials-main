# Generated by Django 4.1.13 on 2024-04-18 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='phone_number',
        ),
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.SmallIntegerField(default=1),
        ),
    ]