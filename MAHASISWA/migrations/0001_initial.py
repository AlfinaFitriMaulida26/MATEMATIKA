# Generated by Django 4.1.2 on 2022-10-15 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mahasiswa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nim', models.CharField(max_length=50)),
                ('nama', models.CharField(max_length=100)),
                ('ttl', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('fakultas', models.CharField(max_length=100)),
                ('prodi', models.CharField(max_length=100)),
                ('alamat', models.CharField(max_length=300)),
                ('foto', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
