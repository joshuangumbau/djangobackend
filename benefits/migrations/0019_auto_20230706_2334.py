# Generated by Django 3.2.16 on 2023-07-06 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('benefits', '0018_bulkplanbenefit_cover_lebal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specialist',
            name='email',
        ),
        migrations.AddField(
            model_name='specialist',
            name='provider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='benefits.provider'),
        ),
        migrations.AddField(
            model_name='specialist',
            name='region',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='specialist',
            name='specialist_location',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='specialist',
            name='specialty',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]
