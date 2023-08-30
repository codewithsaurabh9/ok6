# Generated by Django 4.2.4 on 2023-08-23 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0004_my_skills'),
    ]

    operations = [
        migrations.CreateModel(
            name='education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education_date', models.CharField(blank=True, max_length=150)),
                ('education_name', models.CharField(blank=True, max_length=150)),
                ('education_detail', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience_date', models.CharField(blank=True, max_length=150)),
                ('experience_name', models.CharField(blank=True, max_length=150)),
                ('experience_detail', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='My_Skills2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MySkills', models.CharField(blank=True, max_length=150)),
                ('percent', models.CharField(blank=True, max_length=150)),
                ('width_percent', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='MyServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Servicespng', models.ImageField(upload_to='Services/png')),
                ('Services_name', models.CharField(blank=True, max_length=150)),
                ('Services_detail', models.CharField(blank=True, max_length=150)),
            ],
        ),
    ]