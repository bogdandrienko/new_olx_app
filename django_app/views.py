from django.shortcuts import render, redirect
from django.urls import reverse

from django_app import models


def home(request):
    all_ads = models.Ad.objects.all()
    context = {"name": "Bogdan", "all_ads": all_ads}
    return render(request, "django_app/home.html", context=context)


def public(request):
    if request.method == "GET":
        return render(request, "django_app/public.html")
    elif request.method == "POST":
        title = request.POST.get("title", None)
        description = request.POST.get("description", None)
        price = request.POST.get("price", None)

        models.Ad.objects.create(
            title=title,
            description=description,
            price=price
        )

        return redirect(reverse('home'))
