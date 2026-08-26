from django.shortcuts import render, get_object_or_404
from .models import About


def about(request):
    # There shouldn't be more than one About row, but limit it just in case
    queryset = About.objects.all()[:1]
    about = get_object_or_404(queryset)

    return render(
        request,
        "about/about.html",
        {"about": about},
    )
