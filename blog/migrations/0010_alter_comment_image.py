# Generated by Django 4.2.1 on 2023-05-29 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_comment_image_alter_comment_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=models.ImageField(default='avatar/2023/05/29/115-1150821_default-avatar-comments-sign-in-icon.png', upload_to='avatar/%Y/%m/%d/'),
        ),
    ]