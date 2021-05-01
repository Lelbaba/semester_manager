# Generated by Django 3.2 on 2021-04-27 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_routineclass'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routineclass',
            name='weekday',
            field=models.CharField(choices=[('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')], default='Sunday', max_length=10),
        ),
    ]