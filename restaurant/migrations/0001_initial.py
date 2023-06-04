# Generated by Django 4.2 on 2023-06-04 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250, verbose_name='Nombre')),
                ('categoria', models.PositiveSmallIntegerField(choices=[(10, 'Basico'), (20, 'Premium')], verbose_name='Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250, verbose_name='Nombre')),
                ('precio', models.PositiveSmallIntegerField(verbose_name='Precio')),
                ('activo', models.BooleanField(default=True, verbose_name='Activo')),
                ('ingredientes', models.ManyToManyField(related_name='ingredientes', to='restaurant.ingrediente', verbose_name='Ingredientes')),
            ],
        ),
    ]
