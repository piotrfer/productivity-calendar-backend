# Generated by Django 3.0.6 on 2020-05-18 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('duration', models.IntegerField()),
                ('start', models.TimeField()),
                ('category', models.CharField(choices=[('WRK', 'work'), ('SCH', 'school'), ('HOB', 'hobby'), ('SOC', 'social'), ('NED', 'needs'), ('FUN', 'fun'), ('REL', 'relax')], max_length=3)),
                ('day', models.CharField(choices=[('MON', 'monday'), ('TUE', 'tuesday'), ('WED', 'wednesday'), ('THU', 'thursday'), ('FRI', 'friday'), ('SAT', 'saturday'), ('SUN', 'sunday')], max_length=3)),
            ],
        ),
    ]