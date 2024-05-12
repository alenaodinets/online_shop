from django.core.management import BaseCommand
from catalog.models import Blogpost
import json


class Command(BaseCommand):

    @staticmethod
    def json_read_catalog():
        with open("blogpost.json", encoding="UTF-8") as file:
            data = json.load(file)
            return data

    def handle(self, *args, **options):
        Blogpost.objects.all().delete()

        catalog_for_create = []

        for blogpost in Command.json_read_catalog():
            catalog_for_create.append(
                Blogpost(
                    id=blogpost["pk"],
                    title=blogpost["title"],
                    slug=blogpost["slug"],
                    content=blogpost["content"],
                    preview=blogpost["preview"],
                    created_at=blogpost["created_at"],
                )
            )
        Blogpost.objects.bulk_create(catalog_for_create)

