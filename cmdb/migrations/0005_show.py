# Generated by Django 2.1 on 2018-09-28 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0004_userinfo_tel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=1000)),
                ('shopname', models.TextField(default='', max_length=1000)),
                ('price', models.IntegerField()),
                ('pinglun', models.IntegerField()),
                ('hit', models.IntegerField(default=0)),
            ],
        ),
    ]