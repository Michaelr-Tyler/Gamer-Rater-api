# Generated by Django 3.1.3 on 2020-11-03 20:14

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
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('duration', models.CharField(max_length=50)),
                ('release_year', models.IntegerField()),
                ('number_of_players', models.IntegerField()),
                ('age_restrictions', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=500)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=250)),
                ('rating', models.IntegerField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterapi.game')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterapi.player')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=None)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterapi.game')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterapi.player')),
            ],
        ),
        migrations.CreateModel(
            name='Gamecategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterapi.category')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterapi.game')),
            ],
        ),
        migrations.CreateModel(
            name='Designer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterapi.game')),
            ],
        ),
    ]
