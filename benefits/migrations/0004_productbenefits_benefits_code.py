# Generated by Django 3.2.19 on 2023-05-24 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('benefits', '0003_benefitdetails_productbenefits'),
    ]

    operations = [
        migrations.AddField(
            model_name='productbenefits',
            name='benefits_code',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]
