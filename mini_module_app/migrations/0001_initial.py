# Generated by Django 3.2 on 2021-10-07 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50, verbose_name='Предмет')),
                ('type', models.CharField(max_length=50, verbose_name='Тип')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('file', models.FileField(upload_to='', verbose_name='Файл')),
            ],
            options={
                'verbose_name': 'Файл',
                'verbose_name_plural': 'Файлы',
                'ordering': ['-title'],
            },
        ),
    ]
