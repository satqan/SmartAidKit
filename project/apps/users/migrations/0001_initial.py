# Generated by Django 4.1.3 on 2022-11-06 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=20, verbose_name='Username')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('first_name', models.CharField(max_length=30, verbose_name='First name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='Last name')),
                ('middle_name', models.CharField(blank=True, max_length=30, verbose_name='Middle name')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]