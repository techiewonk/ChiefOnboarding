from django.contrib.auth import get_user_model
from django.db import models
from django.template.loader import render_to_string
from django.urls import reverse

from misc.models import Content
from misc.fields import ContentJSONField
from organization.models import BaseItem


class ToDo(BaseItem):
    content = models.ManyToManyField(Content)
    content_json = ContentJSONField(default=dict)
    due_on_day = models.IntegerField(default=0)
    form = models.JSONField(default=list)
    # Chat bot specific actions
    send_back = models.BooleanField(default=False)
    slack_channel = models.ForeignKey(
        "slack_bot.SlackChannel", null=True, on_delete=models.SET_NULL
    )

    @property
    def get_icon_template(self):
        return render_to_string("_todo_icon.html")

    def update_url(self):
        return reverse("todo:update", args=[self.id])

    def delete_url(self):
        return reverse("todo:delete", args=[self.id])

    def get_slack_form(self):
        slack_form_items = []
        for i in self.form:
            options = []
            if i["type"] == "select":
                for j in i["options"]:
                    options.append(
                        {
                            "text": {
                                "type": "plain_text",
                                "text": j["name"],
                                "emoji": True,
                                # "action_id": j['id']
                            },
                            "value": j["name"],
                        }
                    )
                slack_form_items.append(
                    {
                        "type": "input",
                        "block_id": i["id"],
                        "element": {
                            "type": "static_select",
                            "placeholder": {
                                "type": "plain_text",
                                "text": "Select an item",
                                "emoji": True,
                            },
                            "options": options,
                            "action_id": i["id"],
                        },
                        "label": {
                            "type": "plain_text",
                            "text": i["text"],
                            "emoji": True,
                        },
                    }
                )
            if i["type"] == "input":
                slack_form_items.append(
                    {
                        "type": "input",
                        "block_id": i["id"],
                        "element": {"type": "plain_text_input", "action_id": i["id"]},
                        "label": {
                            "type": "plain_text",
                            "text": i["text"],
                            "emoji": True,
                        },
                    }
                )
            if i["type"] == "text":
                slack_form_items.append(
                    {
                        "type": "input",
                        "block_id": i["id"],
                        "element": {
                            "type": "plain_text_input",
                            "multiline": True,
                            "action_id": i["id"],
                        },
                        "label": {
                            "type": "plain_text",
                            "text": i["text"],
                            "emoji": True,
                        },
                    }
                )
        return slack_form_items

    def valid_for_slack(self):
        valid = True
        for i in self.form:
            if i["type"] == "check" or i["type"] == "upload":
                valid = False
                break
        return valid
