# Generated by Django 5.1.2 on 2024-12-02 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userblog', '0005_alter_post_state_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='state_type',
            field=models.CharField(choices=[('active', 'ativo'), ('archived', 'arquivado'), ('deleted', 'deletado')], default='active', max_length=10, verbose_name='Estado do post'),
        ),
    ]