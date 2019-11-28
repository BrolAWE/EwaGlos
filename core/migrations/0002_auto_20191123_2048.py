# Generated by Django 2.2.7 on 2019-11-23 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sectiontranslation',
            name='language',
            field=models.CharField(choices=[('BG', 'Bulgarian'), ('DE', 'German'), ('EN', 'English'), ('ES', 'Spanish'), ('FR', 'French'), ('HR', 'Croatian'), ('HU', 'Hungarian'), ('IT', 'Italian'), ('RO', 'Romanian'), ('RU', 'Russian'), ('TR', 'Turkish'), ('PL', 'Polish')], max_length=2, verbose_name='Выбрать язык'),
        ),
        migrations.AlterField(
            model_name='subsectiontranslation',
            name='language',
            field=models.CharField(choices=[('BG', 'Bulgarian'), ('DE', 'German'), ('EN', 'English'), ('ES', 'Spanish'), ('FR', 'French'), ('HR', 'Croatian'), ('HU', 'Hungarian'), ('IT', 'Italian'), ('RO', 'Romanian'), ('RU', 'Russian'), ('TR', 'Turkish'), ('PL', 'Polish')], max_length=2, verbose_name='Выбрать язык'),
        ),
        migrations.AlterField(
            model_name='wordtranslation',
            name='language',
            field=models.CharField(choices=[('BG', 'Bulgarian'), ('DE', 'German'), ('EN', 'English'), ('ES', 'Spanish'), ('FR', 'French'), ('HR', 'Croatian'), ('HU', 'Hungarian'), ('IT', 'Italian'), ('RO', 'Romanian'), ('RU', 'Russian'), ('TR', 'Turkish'), ('PL', 'Polish')], max_length=2, verbose_name='Выбрать язык'),
        ),
        migrations.CreateModel(
            name='Synonym',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('synonym', models.CharField(max_length=100, verbose_name='Синоним')),
                ('word', models.ForeignKey(help_text='Choose from the list the word', on_delete=django.db.models.deletion.CASCADE, to='core.WordTranslation', verbose_name='Исходное слово')),
            ],
            options={
                'verbose_name': 'Синоним',
                'verbose_name_plural': 'Синонимы',
            },
        ),
    ]