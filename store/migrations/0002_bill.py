# Generated by Django 3.1.1 on 2020-09-22 00:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=150)),
                ('nit', models.PositiveIntegerField()),
                ('code', models.PositiveIntegerField()),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.client')),
            ],
        ),
    ]
