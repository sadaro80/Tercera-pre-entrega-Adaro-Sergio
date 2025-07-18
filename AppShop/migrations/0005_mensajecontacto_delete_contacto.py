# Generated by Django 5.2.4 on 2025-07-16 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppShop', '0004_cliente_delete_clientes'),
    ]

    operations = [
        migrations.CreateModel(
            name='MensajeContacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mensaje', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='contacto',
        ),
    ]
