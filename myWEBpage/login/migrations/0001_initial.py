# Generated by Django 2.2.12 on 2021-01-04 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField(max_length=7)),
                ('name', models.CharField(max_length=10)),
            ],
        ),
    ]