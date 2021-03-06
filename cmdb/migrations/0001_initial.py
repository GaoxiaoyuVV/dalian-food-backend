# Generated by Django 2.1.4 on 2019-05-26 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=1000)),
                ('shopname', models.TextField(default='', max_length=1000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('pinglun', models.IntegerField()),
                ('hit', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=64)),
                ('tel', models.CharField(max_length=12)),
                ('role', models.CharField(max_length=12)),
            ],
        ),
    ]
