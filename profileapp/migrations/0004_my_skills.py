# Generated by Django 4.2.4 on 2023-08-23 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0003_aboutproject'),
    ]

    operations = [
        migrations.CreateModel(
            name='My_Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MySkills', models.CharField(blank=True, max_length=150)),
                ('percent', models.CharField(blank=True, max_length=150)),
                ('width_percent', models.CharField(blank=True, max_length=150)),
            ],
        ),
    ]