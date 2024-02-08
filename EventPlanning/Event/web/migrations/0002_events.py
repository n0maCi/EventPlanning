# Generated by Django 5.0.1 on 2024-02-08 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, verbose_name='Название мероприятия')),
                ('name', models.CharField(max_length=25, verbose_name='Название собятия')),
                ('place', models.CharField(max_length=50, verbose_name='Место')),
                ('start_at', models.CharField(max_length=5, verbose_name='Начало')),
                ('end_at', models.CharField(max_length=5, verbose_name='Конец')),
                ('full_text', models.TextField(verbose_name='Описание')),
                ('web_buyer_id', models.IntegerField()),
            ],
        ),
    ]