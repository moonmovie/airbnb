# Generated by Django 2.2.5 on 2020-01-14 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0007_auto_20200112_0358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='rooom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='rooms.Room'),
        ),
    ]
