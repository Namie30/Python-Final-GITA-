# Generated by Django 5.1.7 on 2025-03-27 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
