# Generated by Django 4.0.2 on 2022-02-14 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deepthought',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thought_text', models.CharField(max_length=200)),
            ],
        ),
    ]
