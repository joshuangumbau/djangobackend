# Generated by Django 3.2.16 on 2023-02-26 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_accountmodel_approval_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountmodel',
            name='passcode',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
