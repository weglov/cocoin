# Generated by Django 2.0 on 2018-01-12 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_squashed_0019_auto_20180111_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='coin',
            name='market_cap_usd',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=16, verbose_name='Market cap'),
        ),
        migrations.AddField(
            model_name='coin',
            name='supply',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=16, verbose_name='Total Supply'),
        ),
        migrations.AddField(
            model_name='coin',
            name='volume_24h',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=16, verbose_name='Volume 24'),
        ),
    ]