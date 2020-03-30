# Generated by Django 2.0.7 on 2020-03-27 18:18

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
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('title', models.CharField(max_length=60)),
                ('header_title', models.CharField(max_length=60)),
                ('header_subtitle', models.CharField(max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='content',
            name='page_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Page'),
        ),
    ]