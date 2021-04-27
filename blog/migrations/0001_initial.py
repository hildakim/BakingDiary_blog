# Generated by Django 3.2 on 2021-04-27 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_title', models.CharField(max_length=200)),
                ('nickname', models.CharField(max_length=100)),
                ('upload_date', models.DateTimeField()),
                ('recipe', models.TextField()),
            ],
        ),
    ]
