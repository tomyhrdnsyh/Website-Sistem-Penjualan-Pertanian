# Generated by Django 3.2.16 on 2022-11-15 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_customuser_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'pengguna', 'verbose_name_plural': 'pengguna'},
        ),
    ]
