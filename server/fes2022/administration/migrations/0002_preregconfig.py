# Generated by Django 4.1 on 2022-10-28 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fes2022', '0002_campus_room_collaboration'),
        ('administration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreregConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(default=100, verbose_name='一度に表示される量')),
                ('exclusion', models.ManyToManyField(blank=True, to='fes2022.namecarddesign')),
            ],
        ),
    ]
