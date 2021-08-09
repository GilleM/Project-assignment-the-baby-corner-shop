from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from profiles.models import UserProfile


class Testimonial(models.Model):
    """
    Testimonial model for keeping track
    of user testimonials and reviews
    """
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    description = models.TextField()
    grade = models.IntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(5),
    ])
    img_url = models.URLField(default="https://picsum.photos/1000/")
    date = models.DateTimeField(auto_now_add=True)


class Feedback(models.Model):
    """
    ItemRequest model for tracking item requests
    """
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    implemented = models.BooleanField(default=False)
