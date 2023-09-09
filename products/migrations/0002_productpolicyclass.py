# Generated by Django 3.2.19 on 2023-05-19 19:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductPolicyClass',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('policy_name', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('policy_description', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
