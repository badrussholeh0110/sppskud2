# Generated by Django 3.1.5 on 2021-07-27 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setor', '0008_petugas_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unit',
            name='kode',
        ),
        migrations.AddField(
            model_name='unit',
            name='alamaunit',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
