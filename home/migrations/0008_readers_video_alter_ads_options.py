# Generated by Django 4.2.7 on 2023-11-09 04:16

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_newspaper'),
    ]

    operations = [
        migrations.CreateModel(
            name='Readers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name': 'Читатель',
                'verbose_name_plural': 'Читатель',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('added', models.DateTimeField(auto_now=True)),
                ('url', embed_video.fields.EmbedVideoField()),
            ],
            options={
                'verbose_name': 'Видео',
                'verbose_name_plural': 'Видео',
                'ordering': ['-added'],
            },
        ),
        migrations.AlterModelOptions(
            name='ads',
            options={'ordering': ('-id',), 'verbose_name': 'Обявление', 'verbose_name_plural': 'Обявление'},
        ),
    ]
