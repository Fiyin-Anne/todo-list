# Generated by Django 3.0.2 on 2020-02-28 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0004_remove_todo_due_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='status',
            new_name='complete',
        ),
    ]