# Generated by Django 2.2.7 on 2019-11-17 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Use the following format: <em>Name of the section</em>.', max_length=100)),
                ('color', models.CharField(help_text='Use the following format: <em>#00FF00</em>.', max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Subsection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Use the following format: <em>Name of the subsection</em>.', max_length=100)),
                ('color', models.CharField(help_text='Use the following format: <em>#00FF00</em>.', max_length=7)),
                ('section', models.ForeignKey(db_column='section', on_delete=django.db.models.deletion.CASCADE, to='core.Section')),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Use the following format: <em>Word</em>.', max_length=100)),
                ('definition', models.TextField(help_text='Write down the whole definition.')),
                ('comment', models.TextField(help_text='Write some notes about the exhibit in the picture')),
                ('subsection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Subsection')),
            ],
        ),
        migrations.CreateModel(
            name='WordTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('BG', 'Bulgarian'), ('DE', 'German'), ('EN', 'English'), ('ES', 'Spanish'), ('FR', 'French'), ('HR', 'Croatian'), ('HU', 'Hungarian'), ('IT', 'Italian'), ('RO', 'Romanian'), ('RU', 'Russian'), ('TR', 'Turkish')], help_text='Choose the language from the list', max_length=2)),
                ('name', models.CharField(help_text='Write down the translation.', max_length=100)),
                ('definition', models.TextField(help_text='Write down the whole definition.')),
                ('comment', models.TextField(help_text='Write some notes about the exhibit in the picture')),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Word')),
            ],
        ),
        migrations.CreateModel(
            name='SubsectionTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('BG', 'Bulgarian'), ('DE', 'German'), ('EN', 'English'), ('ES', 'Spanish'), ('FR', 'French'), ('HR', 'Croatian'), ('HU', 'Hungarian'), ('IT', 'Italian'), ('RO', 'Romanian'), ('RU', 'Russian'), ('TR', 'Turkish')], max_length=2)),
                ('name', models.CharField(max_length=100)),
                ('subsection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Subsection')),
            ],
        ),
        migrations.CreateModel(
            name='SectionTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('BG', 'Bulgarian'), ('DE', 'German'), ('EN', 'English'), ('ES', 'Spanish'), ('FR', 'French'), ('HR', 'Croatian'), ('HU', 'Hungarian'), ('IT', 'Italian'), ('RO', 'Romanian'), ('RU', 'Russian'), ('TR', 'Turkish')], max_length=2)),
                ('name', models.CharField(max_length=100)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Section')),
            ],
        ),
        migrations.CreateModel(
            name='CloseSenseWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('close_sense', models.ForeignKey(help_text='Choose from the list close sense word', on_delete=django.db.models.deletion.CASCADE, related_name='close_sense', to='core.Word')),
                ('word', models.ForeignKey(help_text='Choose from the list the word', on_delete=django.db.models.deletion.CASCADE, related_name='word', to='core.Word')),
            ],
        ),
    ]
