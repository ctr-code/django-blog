from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import About
from .forms import CollaborationForm


def about(request):
    """
    Render the about page and accept user collaboration requests.
    Displays the single instance of :model:`about.About`.
    **Context**
    ``about``
        The single instance of :model:`about.About`.
    ``collaboration_form``
        An instance of :form:`about.CollaborationForm`.
    **Template:**
    :template:`about/about.html`
    """
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
