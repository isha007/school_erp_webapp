# Generated by Django 2.2.2 on 2019-08-20 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentcomponents', '0008_remove_studentdetail_other_languages_known'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentpaidrecord',
            name='fees_paid_type',
            field=models.CharField(max_length=50, verbose_name='Payment Type:'),
        ),
    ]
