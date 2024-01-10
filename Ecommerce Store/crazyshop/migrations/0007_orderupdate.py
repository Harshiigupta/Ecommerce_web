# Generated by Django 2.1.5 on 2019-02-21 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crazyshop', '0006_orders_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderUpdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default='')),
                ('update_desc', models.CharField(max_length=5000)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
