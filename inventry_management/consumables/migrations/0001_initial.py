# Generated by Django 4.1 on 2022-08-04 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewItem',
            fields=[
                ('new_item_id', models.AutoField(primary_key=True, serialize=False)),
                ('new_item_name', models.CharField(max_length=100, unique=True)),
                ('new_item_Created_Date', models.DateField(auto_now=True)),
                ('category_name', models.CharField(choices=[('FOOD_AND_DRINK', 'FOOD_AND_DRINK'), ('HOUSEKEEPING', 'HOUSEKEEPING'), ('ELECTRIC_GOODS', 'ELECTRIC_GOODS'), ('STATIONARY', 'STATIONARY'), ('SAFETY', 'SAFETY'), ('OTHER', 'OTHER')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('qty', models.IntegerField()),
                ('shelf_life', models.DateField()),
                ('dates', models.DateField(auto_now=True)),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='item', to='consumables.newitem')),
            ],
        ),
        migrations.CreateModel(
            name='DeletedItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('del_qty', models.IntegerField()),
                ('del_items', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='consumables.newitem')),
            ],
        ),
    ]