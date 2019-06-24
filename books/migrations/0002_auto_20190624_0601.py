# Generated by Django 2.0.2 on 2019-06-24 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='data_published',
        ),
        migrations.AddField(
            model_name='book',
            name='year',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
