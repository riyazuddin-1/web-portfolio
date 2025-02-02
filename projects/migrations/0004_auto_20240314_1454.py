# Generated by Django 3.2.25 on 2024-03-14 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20240306_1248'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='projectdetails',
            name='codeLink',
        ),
        migrations.RemoveField(
            model_name='projectdetails',
            name='deployedLink',
        ),
        migrations.RemoveField(
            model_name='projectdetails',
            name='designLink',
        ),
        migrations.AddField(
            model_name='projectdetails',
            name='additional_description',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='projectdetails',
            name='techused',
            field=models.CharField(max_length=400, null=True),
        ),
    ]
