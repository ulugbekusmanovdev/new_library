# Generated by Django 4.2.7 on 2023-11-09 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forlibraries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Irbis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('text', models.TextField()),
            ],
        ),
    ]
