# Generated by Django 4.0.2 on 2022-03-02 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('theme', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('text', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Kelgan Izoxlar',
                'verbose_name_plural': 'Kelgan Izoxlar',
            },
        ),
    ]
