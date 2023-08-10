# Generated by Django 4.2.4 on 2023-08-09 21:55

from django.db import migrations, models
import phonenumber_field.modelfields


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
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('auth_code', models.CharField(max_length=4)),
                ('own_invite_code', models.CharField(max_length=6)),
                ('activated_invite_code', models.CharField(blank=True, default='', max_length=6)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]