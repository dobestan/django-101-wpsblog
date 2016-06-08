from django.shortcuts import render


def signup(request):
    return render(
        request,
        "auth/signup.html",
        {},
    )
