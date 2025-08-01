# Generated by Django 5.2.4 on 2025-07-28 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MediaFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='media/')),
                ('file_type', models.CharField(choices=[('image', 'Image'), ('audio', 'Audio'), ('video', 'Video')], max_length=10)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
