# Generated by Django 3.0.1 on 2020-02-15 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200215_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotation',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
