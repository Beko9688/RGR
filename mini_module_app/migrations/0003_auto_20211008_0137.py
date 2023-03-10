# Generated by Django 3.2 on 2021-10-07 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini_module_app', '0002_alter_files_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10, verbose_name='Заголовок')),
                ('note', models.CharField(max_length=250, verbose_name='Заметка')),
            ],
            options={
                'verbose_name': 'Заметка',
                'verbose_name_plural': 'Заметки',
                'ordering': ['-title'],
            },
        ),
        migrations.AlterField(
            model_name='files',
            name='subject',
            field=models.CharField(choices=[('Парадигмы', 'Парадигмы'), ('Копьютерные сети', 'Копьютерные сети'), ('Человек и компьютер', 'Человек и компьютер')], max_length=50, verbose_name='Предмет'),
        ),
        migrations.AlterField(
            model_name='files',
            name='type',
            field=models.CharField(choices=[('Лекция', 'Лекция'), ('Практика', 'Практика'), ('Лабораторная', 'Лабораторная')], max_length=50, verbose_name='Тип'),
        ),
    ]
