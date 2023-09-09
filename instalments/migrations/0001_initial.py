# Generated by Django 3.2.19 on 2023-05-20 03:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IBSPayer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('payer_name', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('payer_address', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('payer_logo', models.TextField(blank=True, default='', max_length=200, null=True)),
                ('physical_address', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('payer_code', models.CharField(blank=True, max_length=200, null=True)),
                ('latitude', models.FloatField(blank=True, default=0)),
                ('logitude', models.FloatField(blank=True, default=0)),
                ('phone', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=200, null=True, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('status', models.CharField(blank=True, default='NEW', max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]