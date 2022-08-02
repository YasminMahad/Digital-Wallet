# Generated by Django 4.0.6 on 2022-08-02 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0007_account_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='type',
        ),
        migrations.AlterField(
            model_name='account',
            name='account_type',
            field=models.CharField(choices=[('f', 'fixed account'), ('c', 'current')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='card_type',
            field=models.CharField(choices=[('C', 'Credit Card'), ('D', 'Debit Card')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='issuer',
            field=models.CharField(choices=[('M', 'Master Card'), ('V', 'Visa Card')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(choices=[('D', 'Deposite'), ('W', 'Withdrawal')], max_length=30, null=True),
        ),
    ]
