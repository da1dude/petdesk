# Generated by Django 3.2.12 on 2024-01-22 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_checkin_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rx',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=250)),
                ('treatment', models.TextField(max_length=250)),
            ],
        ),
    ]