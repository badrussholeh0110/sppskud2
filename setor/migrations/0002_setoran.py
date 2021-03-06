# Generated by Django 3.1.5 on 2021-06-24 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setoran',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jumlahsetoran', models.IntegerField(null=True)),
                ('tgl', models.DateTimeField(auto_now_add=True, null=True)),
                ('nama', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='setor.penyetor')),
                ('namapetugas', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='setor.petugas')),
                ('namaunit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='setor.unit')),
            ],
        ),
    ]
