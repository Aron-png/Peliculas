# Generated by Django 4.1.6 on 2023-02-21 00:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0003_pelicula_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('estado', models.CharField(choices=[('A', 'Activo'), ('R', 'Retirado')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='PeliculaXActor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiempo', models.IntegerField(default=0, verbose_name='Tiempo en pantalla')),
                ('sueldo', models.DecimalField(decimal_places=2, default=0.0, max_digits=7)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='endpoints.actor')),
                ('pelicula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='endpoints.pelicula')),
            ],
        ),
    ]
