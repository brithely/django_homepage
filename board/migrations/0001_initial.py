# Generated by Django 2.1 on 2018-08-23 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('num_id', models.AutoField(primary_key=True, serialize=False)),
                ('cont_nm', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id_email', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=128)),
                ('user_name', models.CharField(max_length=15)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField()),
            ],
        ),
    ]