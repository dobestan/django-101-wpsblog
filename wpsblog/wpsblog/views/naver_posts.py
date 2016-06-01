from django.shortcuts import render

from wpsblog.models import NaverPost


def naver_posts_list(request):
    keyword = request.GET.get("keyword")
    naver_posts = NaverPost.objects.all()

    if keyword:
        naver_posts = [
            naver_post
            for naver_post
            in naver_posts
            if naver_post.keyword == keyword
        ]

    return render(
        request,
        "naver_posts/list.html",
        {
            "keyword": keyword,
            "naver_posts": naver_posts,
        },
    )
