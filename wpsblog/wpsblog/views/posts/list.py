from django.shortcuts import render


def list(request):
    return render(
        request,
        "posts/list.html",
        {},
    )
