# Generated by Django 3.2.16 on 2023-07-05 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('benefits', '0017_bulkplanbenefit_productprovider_productspecialist_provider_specialist'),
    ]

    operations = [
        migrations.AddField(
            model_name='bulkplanbenefit',
            name='cover_lebal',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]
