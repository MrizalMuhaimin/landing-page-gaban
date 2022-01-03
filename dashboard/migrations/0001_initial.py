# Generated by Django 3.2.8 on 2021-12-26 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InfoUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('prov', models.CharField(max_length=255)),
                ('kab', models.CharField(max_length=255)),
                ('kec', models.CharField(max_length=255)),
                ('des', models.CharField(max_length=255)),
                ('alamat', models.TextField()),
                ('almamater', models.CharField(max_length=255)),
                ('jurusan', models.CharField(max_length=255)),
                ('angkatan', models.CharField(max_length=4)),
                ('email', models.EmailField(max_length=254)),
                ('nomerTel', models.CharField(max_length=100)),
                ('idline', models.CharField(max_length=255)),
                ('inKerja', models.CharField(max_length=255)),
                ('sektorKerja', models.CharField(max_length=255)),
                ('sektorUsaha', models.CharField(max_length=255)),
                ('infoKontak', models.CharField(choices=[('Telpon/sms', 'telpon/sms'), ('Wa', 'blog'), ('Email', 'berita'), ('Line', 'line')], default='Telpon/sms', max_length=100)),
            ],
        ),
    ]