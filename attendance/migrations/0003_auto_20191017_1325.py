# Generated by Django 2.2.4 on 2019-10-17 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_auto_20191008_1746'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='student',
            unique_together={('first_name', 'last_name')},
        ),
    ]
