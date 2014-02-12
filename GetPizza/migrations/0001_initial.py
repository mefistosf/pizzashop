# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=15)),
                ('login', models.CharField(unique=True, max_length=15)),
                ('password', models.CharField(max_length=15)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25)),
                ('price', models.DecimalField(default=0, max_digits=5, decimal_places=2)),
                ('image', models.ImageField(upload_to='.GetPizza/PizzaImage/')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
