# Generated by Django 3.1.14 on 2023-01-15 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xodim', '0007_auto_20230103_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='about',
            field=models.TextField(default='Xodim :   '),
        ),
    ]
