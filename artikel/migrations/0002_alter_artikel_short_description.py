# Generated by Django 4.1 on 2022-10-28 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artikel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artikel',
            name='short_description',
            field=models.TextField(max_length=60),
        ),
    ]
