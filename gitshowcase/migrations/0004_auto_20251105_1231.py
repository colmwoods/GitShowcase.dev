# Generated manually to add GitHub metadata fields to Bookmark model

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('gitshowcase', '0003_bookmark_description_bookmark_forks_count_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='language',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bookmark',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bookmark',
            name='stargazers_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bookmark',
            name='forks_count',
            field=models.IntegerField(default=0),
        ),
    ]
