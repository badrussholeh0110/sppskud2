# Generated by Django 3.1.5 on 2021-07-12 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setor', '0005_harga'),
    ]

    operations = [
        migrations.AddField(
            model_name='setoran',
            name='harga',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='setor.harga'),
        ),
    ]
