# Generated by Django 3.2.19 on 2023-05-10 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KYC', '0002_alter_kyctemplate_kyc_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kyctemplate',
            name='kyc_name',
            field=models.CharField(blank=True, default='DEFAULT TEMPLATE MODEL', max_length=200, null=True),
        ),
    ]