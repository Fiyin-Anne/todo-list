# Generated by Django 3.0.2 on 2020-02-27 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_auto_20200213_1840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='content',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='date_published',
        ),
        migrations.AddField(
            model_name='todo',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='todo',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='due_date',
            field=models.DateField(default='2020-02-27'),
        ),
    ]