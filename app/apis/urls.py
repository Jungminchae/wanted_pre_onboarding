from django.urls import path
from apis.views.jobpost_views import (
    JobPostRegistrationView,
    JobPostUpdateView,
    JobPostDeleteView,
)


app_name = "apis"

urlpatterns = [
    path(
        "registration/", JobPostRegistrationView.as_view(), name="jobpost_registration"
    ),
    path("update/<int:pk>/", JobPostUpdateView.as_view(), name="jobpost_update"),
    path("delete/<int:pk>/", JobPostDeleteView.as_view(), name="jobpost_delete"),
]
