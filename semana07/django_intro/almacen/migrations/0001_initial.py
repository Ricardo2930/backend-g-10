# Generated by Django 4.1.5 on 2023-01-26 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductosModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('precio', models.FloatField()),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'productos',
            },
        ),
    ]
