from django.shortcuts import render


def detail(request, post_id):
    return render(
        request,
        "posts/detail.html",
        {},
    )
