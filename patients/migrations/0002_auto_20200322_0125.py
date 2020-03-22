# Generated by Django 3.0.4 on 2020-03-22 00:25

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='birthdate',
        ),
        migrations.RemoveField(
            model_name='test',
            name='city',
        ),
        migrations.RemoveField(
            model_name='test',
            name='confirmed',
        ),
        migrations.RemoveField(
            model_name='test',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='test',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='test',
            name='insurance',
        ),
        migrations.RemoveField(
            model_name='test',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='test',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='test',
            name='positive_contact',
        ),
        migrations.RemoveField(
            model_name='test',
            name='tested',
        ),
        migrations.RemoveField(
            model_name='test',
            name='zip',
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(default='', max_length=100)),
                ('lastname', models.CharField(default='', max_length=100)),
                ('birthdate', models.DateField(default=django.utils.timezone.now)),
                ('zip', models.CharField(default='', max_length=100)),
                ('city', models.CharField(default='', max_length=100)),
                ('phone', models.CharField(default='', max_length=100)),
                ('doctor', models.CharField(default='', max_length=100)),
                ('insurance', models.CharField(default='', max_length=100)),
                ('positive_contact', models.BooleanField(default=True)),
                ('tested', models.BooleanField(default=False)),
                ('confirmed', models.BooleanField(default=False)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.Test')),
            ],
        ),
    ]