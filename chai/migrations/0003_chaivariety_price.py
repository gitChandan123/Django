# Generated by Django 5.1.4 on 2024-12-21 08:17
# In other tech-stacks it is called as the schema or in the DB


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0002_chaivariety_date_added_chaivariety_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chaivariety',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]
