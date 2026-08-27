from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import About
from .forms import CollaborationForm


def about(request):
    # There shouldn't be more than one About row, but limit it just in case
    queryset = About.objects.all()[:1]
    about = get_object_or_404(queryset)

    if request.method == "POST":
        collaboration_form = CollaborationForm(data=request.POST)
        if collaboration_form.is_valid():
            collaboration_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your collaboration message has been received and will be seen'
            )

    collaboration_form = CollaborationForm()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaboration_form": collaboration_form,
        }
    )
