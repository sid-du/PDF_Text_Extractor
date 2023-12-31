# Generated by Django 3.1.13 on 2022-10-08 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20221008_0154'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='name',
            new_name='product',
        ),
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='id',
        ),
        migrations.AddField(
            model_name='order',
            name='auto_increment_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='total_quantity',
            field=models.IntegerField(null=True),
        ),
    ]
