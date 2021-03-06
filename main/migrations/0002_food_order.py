# Generated by Django 2.2.4 on 2020-06-24 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=64)),
                ('calories', models.IntegerField()),
                ('fat', models.IntegerField()),
                ('carbs', models.IntegerField()),
                ('fiber', models.IntegerField()),
                ('protein', models.IntegerField()),
                ('image', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_favorite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_favorites', to='main.User')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('total_calorie', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordered_foods', to='main.Food')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='main.User')),
            ],
        ),
    ]
