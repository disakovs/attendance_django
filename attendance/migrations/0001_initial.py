# Generated by Django 2.2.5 on 2019-09-18 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Parkour Ages 5-7', 'Ninja Parkour'), ('Parkour Ages 6-10', 'Pee Wee Parkour'), ('Gymnastics Ages 2-3', 'Little Rabits'), ('Gymnastics Ages 4-5', 'Little Kangaroos'), ('Gymnastics Ages 6-10', 'Level 1&2')], max_length=50)),
                ('age_limit', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('Parkour', 'Parkour'), ('Gymnastics', 'Gymnastics')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.Classroom')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('date', models.DateTimeField(default=models.DateTimeField(auto_now_add=True))),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.Classroom')),
                ('students', models.ManyToManyField(related_name='attendances', to='attendance.Student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.Teacher')),
            ],
        ),
    ]