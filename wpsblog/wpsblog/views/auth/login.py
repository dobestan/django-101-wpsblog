from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login


def login(request):
    if (request.method == "POST"):
        username = request.POST.get("username")
        password = request.POST.get("password")
        next_page = request.POST.get("next_page") or reverse("auth:mypage")

        user = authenticate(username=username, password=password)

        if user:
            auth_login(request, user)
            return redirect(next_page)
        return redirect(reverse("auth:login"))

    return render(
        request,
        "auth/login.html",
        {},
    )
