# Generated by Django 4.0.3 on 2022-03-30 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0003_remove_task_due_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='day',
            field=models.CharField(choices=[('M', 'Monday'), ('T', 'Tuesday'), ('W', 'Wednesday'), ('Th', 'Thursday'), ('F', 'Friday'), ('Sa', 'Saturday'), ('Su', 'Sunday'), ('X', 'Other')], default='X', max_length=15),
        ),
    ]
