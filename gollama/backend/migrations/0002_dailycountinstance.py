# Generated by Django 3.0.6 on 2020-06-09 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyCountInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
                ('counter', models.IntegerField(default=0)),
                ('shorthand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.ShortHand')),
            ],
            options={
                'unique_together': {('shorthand', 'day')},
            },
        ),
    ]