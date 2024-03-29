# Generated by Django 3.2.19 on 2023-06-03 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('benefits', '0013_inclusivepackage_packagedetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='benefitdetails',
            name='manufacture_year',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='benefitdetails',
            name='product_value',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='productbenefits',
            name='policy_type',
            field=models.CharField(blank=True, default='Healthcare/Motor', max_length=200, null=True),
        ),
    ]
