import requests
from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand

from wpsblog.models import NaverPost


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("query", type=str)

    def handle(self, *args, **options):
        query = options.get("query")

        self.stdout.write("네이버에서 {query} 블로그 포스트를 크롤링합니다.".format(
            query=query,
        ))

        url = "https://search.naver.com/search.naver?where=post&query={query}".format(
            query=query,
        )

        response = requests.get(url)
        dom = BeautifulSoup(response.text, "html.parser")

        post_elements = dom.select(".sh_blog_top")

        for post_element in post_elements:
            title_element = post_element.select_one(".sh_blog_title")
            title = title_element.text
            url = title_element.get("href")

            content_element = post_element.select_one(".sh_blog_passage")
            content = content_element.text

            thumbnail_image_element = post_element.select_one(".sh_blog_thumbnail")
            thumbnail_image_url = thumbnail_image_element.get("src")

            NaverPost.objects.create(
                keyword=query,
                title=title,
                original_url=url,
                content=content,
                thumbnail_image_url=thumbnail_image_url,
            )
