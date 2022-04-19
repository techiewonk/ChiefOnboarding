# Generated by Django 3.2.12 on 2022-04-19 22:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("slack_bot", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("organization", "0012_auto_20220221_1338"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Changelog",
        ),
        migrations.AlterField(
            model_name="notification",
            name="notification_type",
            field=models.CharField(
                choices=[
                    ("added_todo", "A new to do item has been added"),
                    ("completed_todo", "To do item has been marked as completed"),
                    ("added_resource", "A new resource item has been added"),
                    ("completed_course", "Course has been completed"),
                    ("added_badge", "A new badge item has been added"),
                    ("added_introduction", "A new introduction item has been added"),
                    ("added_preboarding", "A new preboarding item has been added"),
                    ("added_new_hire", "A new hire has been added"),
                    ("added_administrator", "A new administrator has been added"),
                    ("added_manager", "A new manager has been added"),
                    ("added_admin_task", "A new admin task has been added"),
                    ("sent_email_message", "A new email has been sent"),
                    ("sent_text_message", "A new text message has been sent"),
                    ("sent_slack_message", "A new slack message has been sent"),
                    (
                        "failed_no_phone",
                        "Couldn't sent text message: number is missing",
                    ),
                ],
                default="added_todo",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="organization",
            name="ask_colleague_welcome_message",
            field=models.BooleanField(
                default=True,
                verbose_name=(
                    "Send a Slack message to the team to collect personal "
                    "welcome messages from colleages."
                ),
            ),
        ),
        migrations.AlterField(
            model_name="organization",
            name="auto_create_user",
            field=models.BooleanField(
                default=False,
                help_text="If the user does not exist yet",
                verbose_name="Create a new hire when they join your Slack team",
            ),
        ),
        migrations.AlterField(
            model_name="organization",
            name="create_new_hire_without_confirm",
            field=models.BooleanField(
                default=False,
                verbose_name="Create new hires without needing confirm from a user",
            ),
        ),
        migrations.AlterField(
            model_name="organization",
            name="send_new_hire_start_reminder",
            field=models.BooleanField(
                default=False,
                verbose_name=(
                    "Send a Slack message to the team on the day the new hire starts"
                ),
            ),
        ),
        migrations.AlterField(
            model_name="organization",
            name="slack_buttons",
            field=models.BooleanField(
                default=True,
                verbose_name=(
                    "Add 'todo' and 'resource' buttons to the first message that's "
                    "being sent to the new hire."
                ),
            ),
        ),
        migrations.AlterField(
            model_name="organization",
            name="slack_confirm_person",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="User to sent new hire account requests to",
            ),
        ),
        migrations.AlterField(
            model_name="organization",
            name="slack_default_channel",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="slack_bot.slackchannel",
                verbose_name=(
                    "This is the default channel where the bot will post messages in"
                ),
            ),
        ),
    ]
