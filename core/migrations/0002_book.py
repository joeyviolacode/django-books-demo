# Generated by Django 4.0.5 on 2022-06-11 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=63)),
                ('year', models.IntegerField()),
                ('description', models.CharField(max_length=5000)),
            ],
        ),
    ]
