# Generated by Django 3.2.16 on 2023-02-26 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_accountmodel_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountmodel',
            name='approval_status',
            field=models.CharField(blank=True, default='NO', max_length=200, null=True),
        ),
    ]
