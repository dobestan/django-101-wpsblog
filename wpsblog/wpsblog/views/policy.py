from django.shortcuts import render


def terms(request):
    return render(
        request,
        "policy/terms.html",
        {},
    )


def privacy(request):
    return render(
        request,
        "policy/privacy.html",
        {},
    )


def disclaimer(request):
    return render(
        request,
        "policy/disclaimer.html",
        {},
    )
