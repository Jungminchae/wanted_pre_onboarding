from django.urls import path
from apis.views.jobpost_views import (
    JobPostRegistrationView,
    JobPostUpdateView,
    JobPostRetrieveView,
    JobPostDeleteView,
    JobPostReadView,
)
from apis.views.apply_views import ApplyView, ApplyDeleteView


app_name = "apis"

urlpatterns = [
    path("", JobPostReadView.as_view(), name="jobpost_read"),
    path(
        "registration/", JobPostRegistrationView.as_view(), name="jobpost_registration"
    ),
    path("update/<int:pk>/", JobPostUpdateView.as_view(), name="jobpost_update"),
    path("delete/<int:pk>/", JobPostDeleteView.as_view(), name="jobpost_delete"),
    path("<int:pk>/", JobPostRetrieveView.as_view(), name="jobpost_retrieve"),
    path("apply/", ApplyView.as_view(), name="job_apply"),
    path("apply/<int:pk>/", ApplyDeleteView.as_view(), name="job_apply_delete"),
]
