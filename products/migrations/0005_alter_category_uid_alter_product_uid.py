# Generated by Django 5.1.1 on 2024-09-20 20:15

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_category_uid_product_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, null=True, unique=True),
        ),
    ]
