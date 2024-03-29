# Generated by Django 3.2.16 on 2023-06-24 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_auto_20230624_0738'),
    ]

    operations = [
        migrations.RenameField(
            model_name='policies',
            old_name='interim_number',
            new_name='approved_by',
        ),
        migrations.AddField(
            model_name='customerorder',
            name='order_amount',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='policies',
            name='business_type',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='policies',
            name='client_group',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='policies',
            name='document_no',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='policies',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='policies',
            name='policy_amount',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='policies',
            name='policy_type',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='policies',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
