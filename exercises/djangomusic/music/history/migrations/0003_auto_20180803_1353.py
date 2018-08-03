# Generated by Django 2.1 on 2018-08-03 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0002_auto_20180802_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='song',
            name='album',
        ),
        migrations.RemoveField(
            model_name='song',
            name='genre',
        ),
        migrations.AlterField(
            model_name='album',
            name='label',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='album',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='artist',
            name='artist_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='genre',
            name='style',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.DeleteModel(
            name='Song',
        ),
        migrations.AddField(
            model_name='songs',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='history.Album'),
        ),
        migrations.AddField(
            model_name='songs',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='history.Artist'),
        ),
        migrations.AddField(
            model_name='songs',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='history.Genre'),
        ),
    ]