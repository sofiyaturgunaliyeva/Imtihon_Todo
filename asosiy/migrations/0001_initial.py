# Generated by Django 4.2 on 2023-05-09 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=50)),
                ('yosh', models.SmallIntegerField()),
                ('kurs', models.SmallIntegerField()),
                ('student_raqami', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('batafsil_malumot', models.CharField(blank=True, max_length=100, null=True)),
                ('bajarilgan', models.BooleanField(default=False)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.student')),
            ],
        ),
    ]