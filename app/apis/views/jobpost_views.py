from rest_framework.generics import CreateAPIView
from apis.models import JobPost, User, Company
from apis.serializers.jobpost_serializers import JobPostSerializer


class JobPostRegistrationView(CreateAPIView):
    serializer_class = JobPostSerializer
    queryset = JobPost.objects.all()
