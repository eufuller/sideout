# Generated by Django 4.0.6 on 2022-07-13 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('team_name', models.CharField(max_length=100)),
                ('games_played', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Team',
        ),
    ]
