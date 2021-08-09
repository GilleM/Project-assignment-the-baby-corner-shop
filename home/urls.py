from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('feedback', views.feedback, name='feedback'),
    path('feedback/finish/<int:feedback_id>}', views.finish_feedback, name='finish_feedback')
]
