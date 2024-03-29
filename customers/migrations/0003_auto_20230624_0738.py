# Generated by Django 3.2.16 on 2023-06-24 07:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0004_products_policy_class'),
        ('benefits', '0016_alter_productbenefits_policy_type'),
        ('customers', '0002_customer_order_number'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Customer',
            new_name='CustomerOrder',
        ),
        migrations.CreateModel(
            name='Policies',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('policy_number', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('interim_number', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('premiums', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('expiry', models.DateTimeField(auto_now_add=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('benefit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='benefits.productbenefits')),
                ('benefit_details', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='benefits.benefitdetails')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.products')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
