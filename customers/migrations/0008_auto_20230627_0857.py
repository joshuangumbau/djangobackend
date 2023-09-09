# Generated by Django 3.2.16 on 2023-06-27 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instalments', '0007_auto_20230524_1108'),
        ('customers', '0007_alter_policies_policy_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='policies',
            name='currency',
            field=models.CharField(blank=True, default='KSH', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='policies',
            name='payer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='instalments.ibspayer'),
        ),
        migrations.AddField(
            model_name='policies',
            name='requested_by',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='policies',
            name='approved_by',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
