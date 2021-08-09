from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.views.decorators.http import require_POST

from .models import Testimonial, Feedback
from .forms import FeedbackForm


def index(request):
    """ A view to return the index page """
    testimonials = Testimonial.objects.all()

    context = {
        'testimonials': testimonials,
        "is_superuser": request.user.is_superuser,
    }

    if request.user.is_superuser:
        context["feedbacks"] = Feedback.objects.filter(implemented=False)

    return render(request, 'home/index.html', context)


@require_POST
def feedback(request):
    """ Add a new feedback """

    form = FeedbackForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully sent feedback')
        return redirect(reverse("home"))
    else:
        messages.error(request, 'Failed to sent feedback. Please ensure the form is valid.')
    return redirect(reverse("home"))


@require_POST
def finish_feedback(request, feedback_id):
    Feedback.objects.filter(id=feedback_id).update(implemented=True)
    return redirect(reverse("home"))
