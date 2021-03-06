# Generated by Django 2.0.7 on 2020-03-31 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_type', models.CharField(blank=True, choices=[('<p>', 'Paragraph'), ('<li>', 'List'), ('<object>', 'Object'), ('<span>', 'Span Block')], max_length=10)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(unique=True)),
                ('title', models.CharField(max_length=60)),
                ('header_title', models.CharField(max_length=60)),
                ('header_subtitle', models.CharField(blank=True, max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='content',
            name='page_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Page'),
        ),
    ]
