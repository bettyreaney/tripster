# Generated by Django 3.2.4 on 2021-07-24 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_stop'),
    ]

    operations = [
        migrations.AddField(
            model_name='stop',
            name='trip',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.trip'),
            preserve_default=False,
        ),
    ]
