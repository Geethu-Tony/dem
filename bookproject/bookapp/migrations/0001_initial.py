# Generated by Django 3.2.19 on 2023-06-11 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=250)),
                ('genre', models.CharField(max_length=250)),
                ('publication_date', models.DateField()),
                ('avilability', models.BooleanField(default=True)),
            ],
        ),
    ]
