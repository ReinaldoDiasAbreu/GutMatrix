# Generated by Django 3.2.8 on 2021-10-21 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
