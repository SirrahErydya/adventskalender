# Generated by Django 2.2.7 on 2019-11-15 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Window',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField()),
                ('content', models.ImageField(upload_to='')),
                ('open', models.BooleanField(default=False)),
            ],
        ),
    ]
