# Generated by Django 3.0.2 on 2020-02-12 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_published', models.DateTimeField()),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField(blank=True)),
                ('created', models.DateField(default='2020-02-12')),
                ('due_date', models.DateField(default='2020-02-12')),
            ],
        ),
    ]
