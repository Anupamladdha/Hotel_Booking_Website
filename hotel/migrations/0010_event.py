# Generated by Django 3.1.7 on 2021-03-30 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0009_auto_20210330_0639'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=12)),
                ('eventtype', models.CharField(max_length=122)),
                ('eventdate', models.DateField()),
                ('desc', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
