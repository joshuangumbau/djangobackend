# Generated by Django 3.2.16 on 2023-02-26 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_accountmodel_passcode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountmodel',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='accountmodel',
            name='deleted_by',
        ),
        migrations.RemoveField(
            model_name='accountmodel',
            name='deleted_date',
        ),
        migrations.RemoveField(
            model_name='accountmodel',
            name='gender',
        ),
        migrations.AddField(
            model_name='accountmodel',
            name='payment',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='accountmodel',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]