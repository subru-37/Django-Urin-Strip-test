# Generated by Django 5.0.6 on 2024-06-15 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stripColors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagemodel',
            name='name',
            field=models.CharField(default='undefined', max_length=50),
        ),
    ]
