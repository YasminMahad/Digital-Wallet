# Generated by Django 4.0.6 on 2022-08-02 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0010_alter_card_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='loan_type',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
