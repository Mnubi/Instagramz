# Generated by Django 3.2.9 on 2021-12-11 02:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0007_like_unique_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='upvotes', to='insta.image'),
        ),
    ]
