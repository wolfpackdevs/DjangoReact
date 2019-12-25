# Generated by Django 3.0.1 on 2019-12-25 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('endpoints', '0003_persona_eventos'),
    ]

    operations = [
        migrations.CreateModel(
            name='estadoPersonaPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'estados de persona en plan',
            },
        ),
        migrations.CreateModel(
            name='personaPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fue', models.BooleanField(null=True)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personas_planes', to='planes.estadoPersonaPlan')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personas_planes', to='endpoints.persona')),
            ],
            options={
                'verbose_name_plural': 'personas en plan',
            },
        ),
        migrations.CreateModel(
            name='plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planes', to='endpoints.evento')),
                ('personas', models.ManyToManyField(related_name='planes', to='planes.personaPlan')),
            ],
            options={
                'verbose_name_plural': 'planes',
            },
        ),
    ]