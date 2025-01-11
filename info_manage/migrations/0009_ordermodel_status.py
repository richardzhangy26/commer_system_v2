# Generated by Django 4.2.1 on 2025-01-10 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_manage', '0008_carmodel_size_ordermodel_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='status',
            field=models.CharField(choices=[('ordered', '已下单'), ('shipped', '已发货'), ('delivered', '已送达'), ('completed', '已完成')], default='ordered', max_length=20, verbose_name='订单状态'),
        ),
    ]
