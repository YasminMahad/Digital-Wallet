# Generated by Django 4.0.6 on 2022-08-19 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0018_alter_transaction_transactionreciept'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thirdparty',
            old_name='transaction_account',
            new_name='transaction_amount',
        ),
    ]
