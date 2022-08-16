from rest_framework.generics import CreateAPIView, UpdateAPIView
from apis.models import JobPost
from apis.serializers.jobpost_serializers import JobPostSerializer


class JobPostRegistrationView(CreateAPIView):
    serializer_class = JobPostSerializer
    queryset = JobPost.objects.all()


class JobPostUpdateView(UpdateAPIView):
    serializer_class = JobPostSerializer
    queryset = JobPost.objects.all()
