from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("learning_logs", "0003_topic_owner"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Entiy",
            new_name="Entry",
        ),
    ]
