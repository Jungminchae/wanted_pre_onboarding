from django.urls import path
from apis.views.jobpost_views import (
    JobPostRegistrationView,
    JobPostUpdateView,
    JobPostRetrieveDeleteView,
    JobPostReadView,
)


app_name = "apis"

urlpatterns = [
    path("", JobPostReadView.as_view(), name="jobpost_read"),
    path(
        "registration/", JobPostRegistrationView.as_view(), name="jobpost_registration"
    ),
    path("update/<int:pk>/", JobPostUpdateView.as_view(), name="jobpost_update"),
    path(
        "delete/<int:pk>/", JobPostRetrieveDeleteView.as_view(), name="jobpost_delete"
    ),
    path("<int:pk>/", JobPostRetrieveDeleteView.as_view(), name="jobpost_retrieve"),
]
