# Generated by Django 3.1.3 on 2020-11-20 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scrapper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume_file', models.FileField(upload_to='docscrapapp/')),
            ],
        ),
    ]
