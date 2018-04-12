# Generated by Django 2.0.1 on 2018-02-26 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20180214_0011'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Solucion', 'verbose_name_plural': 'Soluciones'},
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Category', verbose_name='Categoría'),
        ),
        migrations.AlterField(
            model_name='post',
            name='link_external_tool',
            field=models.URLField(blank=True, verbose_name='Link de Solución'),
        ),
        migrations.AlterField(
            model_name='post',
            name='public',
            field=models.BooleanField(db_index=True, default=False, verbose_name='Publicar'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(db_index=True, max_length=110, unique=True, verbose_name='Titulo'),
        ),
    ]
