# Generated by Django 3.2.19 on 2023-05-24 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('benefits', '0005_benefitdetails_details_code'),
        ('instalments', '0004_instalmentplan_instament_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instalmentplan',
            name='product',
        ),
        migrations.AddField(
            model_name='instalmentplan',
            name='benefit_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='benefits.productbenefits'),
        ),
    ]
