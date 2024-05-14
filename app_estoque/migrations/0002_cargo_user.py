# Generated by Django 5.0.6 on 2024-05-14 00:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_estoque', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('senha', models.TextField(max_length=255)),
                ('chave_acesso', models.TextField(max_length=3)),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuarios', to='app_estoque.cargo')),
            ],
        ),
    ]
