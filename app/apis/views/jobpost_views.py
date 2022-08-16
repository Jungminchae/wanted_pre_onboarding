from rest_framework.generics import CreateAPIView, UpdateAPIView
from apis.models import JobPost
from apis.serializers.jobpost_serializers import (
    JobPostSerializer,
    JobPostUpdateSerializer,
)


class JobPostRegistrationView(CreateAPIView):
    """
    채용공고 등록
    """

    serializer_class = JobPostSerializer
    queryset = JobPost.objects.all()


class JobPostUpdateView(UpdateAPIView):
    """
    채용공고 수정
    :Company ID 제외, 전부 변경 가능
    """

    serializer_class = JobPostUpdateSerializer
    queryset = JobPost.objects.all()
