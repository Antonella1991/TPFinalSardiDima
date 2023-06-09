# Generated by Django 4.2.1 on 2023-05-28 08:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=256)),
                ('apellido', models.CharField(max_length=256)),
                ('domicilio', models.CharField(max_length=256)),
                ('dni', models.CharField(max_length=20)),
                ('telefono', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('creador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=256)),
                ('cuerpo', models.CharField(default=True, max_length=256)),
                ('autor', models.CharField(max_length=256)),
                ('fecha', models.DateTimeField()),
                ('creador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
