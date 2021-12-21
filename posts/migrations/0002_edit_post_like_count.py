# Generated by Django 4.0 on 2021-12-21 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Edit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created DateTime')),
            ],
            options={
                'db_table': 'outer',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='like_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]