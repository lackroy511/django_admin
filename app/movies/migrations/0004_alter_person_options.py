# Generated by Django 5.0.6 on 2024-06-02 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_alter_filmwork_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'участник', 'verbose_name_plural': 'участники'},
        ),
    ]
