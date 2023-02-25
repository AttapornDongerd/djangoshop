# Generated by Django 4.1.7 on 2023-02-24 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.CharField(blank=True, max_length=255)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'cart',
                'ordering': ('date_added',),
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'หมวดหมู่สินค้า', 'verbose_name_plural': 'ข้อมูลประเภทสินค้า'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',), 'verbose_name': 'สินค้า', 'verbose_name_plural': 'ข้อมูลสินค้า'},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='descriotion',
            new_name='description',
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
            options={
                'db_table': 'cartItem',
            },
        ),
    ]
