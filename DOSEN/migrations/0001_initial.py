# Generated by Django 4.1.2 on 2022-10-15 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dosen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nip', models.CharField(max_length=50)),
                ('nidn', models.CharField(max_length=50, null=True)),
                ('nama', models.CharField(max_length=50)),
                ('jabatan', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100)),
                ('foto', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
