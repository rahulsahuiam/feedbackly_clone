# Generated by Django 3.1.2 on 2020-10-05 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='survey',
            fields=[
                ('surveyId', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=200)),
                ('body', models.CharField(max_length=500)),
                ('recipient', models.CharField(max_length=500)),
                ('yes', models.IntegerField(default=0)),
                ('no', models.IntegerField(default=0)),
                ('_user', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserCredits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('credit', models.CharField(default='0', max_length=10)),
            ],
        ),
    ]
