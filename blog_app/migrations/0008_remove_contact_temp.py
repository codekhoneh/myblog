from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0007_contact'),  # وابستگی به آخرین migration
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
    ]