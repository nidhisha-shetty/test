# Generated by Django 3.1.3 on 2020-11-20 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docscrapapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrapper',
            name='resume_file',
            field=models.FileField(upload_to='images/'),
        ),
    ]
