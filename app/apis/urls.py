from django.urls import path
from apis.views.jobpost_views import JobPostRegistrationView


app_name = "apis"

urlpatterns = [
    path(
        "registration/", JobPostRegistrationView.as_view(), name="jobpost_registration"
    )
]
