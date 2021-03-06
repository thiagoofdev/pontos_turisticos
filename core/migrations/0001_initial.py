# Generated by Django 3.2.7 on 2021-09-24 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('atracoes', '0001_initial'),
        ('enderecos', '0001_initial'),
        ('comentarios', '0001_initial'),
        ('avaliacoes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PontoTuristico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('descricao', models.TextField()),
                ('aprovado', models.BooleanField(default=False)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='pontos_turisticos')),
                ('atracoes', models.ManyToManyField(to='atracoes.Atracoes')),
                ('avaliacoes', models.ManyToManyField(to='avaliacoes.Avaliacao')),
                ('comentarios', models.ManyToManyField(to='comentarios.Comentarios')),
                ('enderecos', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='enderecos.enderecos')),
            ],
        ),
    ]
