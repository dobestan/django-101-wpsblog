from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("query", type=str)

    def handle(self, *args, **options):
        query = options.get("query")

        self.stdout.write("네이버에서 {query} 블로그 포스트를 크롤링합니다.".format(
            query=query,
        ))
