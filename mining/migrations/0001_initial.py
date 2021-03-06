# Generated by Django 2.0.6 on 2018-06-09 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MiningInput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=0, max_length=120)),
                ('cost', models.IntegerField(default=0)),
                ('stage', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Stages',
            fields=[
                ('stage_number', models.IntegerField(primary_key=True, serialize=False)),
                ('processing_cost', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StagesWiseCost',
            fields=[
                ('stage', models.IntegerField(primary_key=True, serialize=False)),
                ('computed_cost', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='mininginput',
            name='stages',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mining.Stages'),
        ),
    ]
