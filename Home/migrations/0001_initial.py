# Generated by Django 5.0 on 2024-02-14 05:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fName', models.CharField(max_length=100)),
                ('lName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mail', models.EmailField(max_length=100)),
                ('Phone', models.IntegerField()),
                ('Name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Home.name')),
            ],
        ),
    ]