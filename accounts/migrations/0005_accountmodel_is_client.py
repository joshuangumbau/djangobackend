# Generated by Django 3.2.16 on 2023-02-25 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20230224_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountmodel',
            name='is_client',
            field=models.BooleanField(default=False),
        ),
    ]
