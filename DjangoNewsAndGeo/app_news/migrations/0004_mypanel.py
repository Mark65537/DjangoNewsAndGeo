# Generated by Django 4.2.4 on 2023-08-27 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0003_alter_news_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyPanel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]