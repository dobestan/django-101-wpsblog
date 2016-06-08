from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login


def login(request):
    if (request.method == "POST"):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            auth_login(request, user)
            return redirect(reverse("home"))
        return redirect(reverse("auth:login"))

    return render(
        request,
        "auth/login.html",
        {},
    )
