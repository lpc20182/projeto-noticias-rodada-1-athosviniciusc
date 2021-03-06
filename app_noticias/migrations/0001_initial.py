# Generated by Django 2.1 on 2018-10-23 22:38

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
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=64)),
                ('slug', models.SlugField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='MensagemDeContato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail')),
                ('mensagem', models.TextField()),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Mensagem de contato',
                'verbose_name_plural': 'Mensagens de contato',
            },
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to='', verbose_name='Imagem')),
                ('titulo', models.CharField(max_length=128, verbose_name='Título')),
                ('conteudo', models.TextField(verbose_name='Conteúdo')),
                ('data_de_publicacao', models.DateTimeField(blank=True, null=True, verbose_name='Data de publicação')),
            ],
            options={
                'verbose_name': 'Notícia',
                'verbose_name_plural': 'Notícias',
            },
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128, verbose_name='Nome')),
                ('data_de_nascimento', models.DateField(blank=True, null=True, verbose_name='Data de nascimento')),
                ('telefone_celular', models.CharField(blank=True, help_text='Número do telefone celular no formato (99) 99999-9999', max_length=15, null=True, verbose_name='Telefone celular')),
                ('telefone_fixo', models.CharField(blank=True, help_text='Número do telefone fixo no formato (99) 9999-9999', max_length=14, null=True, verbose_name='Telefone fixo')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=64)),
                ('slug', models.SlugField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='noticia',
            name='autor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='noticias', to='app_noticias.Pessoa'),
        ),
        migrations.AddField(
            model_name='noticia',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_noticias.Categoria'),
        ),
        migrations.AddField(
            model_name='noticia',
            name='tags',
            field=models.ManyToManyField(to='app_noticias.Tag'),
        ),
    ]
