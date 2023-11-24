# Generated by Django 4.2.7 on 2023-11-19 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0003_amplificadores_monitores_notebooks_usuarios_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuarios',
        ),
        migrations.AddField(
            model_name='amplificadores',
            name='descripcion',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='amplificadores',
            name='user',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='monitores',
            name='descripcion',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='monitores',
            name='user',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='notebooks',
            name='descripcion',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='notebooks',
            name='user',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
