# Generated by Django 4.2.3 on 2023-07-24 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_services_category_services_is_home_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='is_home',
            field=models.BooleanField(default=1, verbose_name='Ana Sayfada Gösterilsin Mi?'),
            preserve_default=False,
        ),
    ]
