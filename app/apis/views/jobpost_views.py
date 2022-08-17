from rest_framework.generics import (
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    ListAPIView,
)
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


class JobPostDeleteView(DestroyAPIView):
    """
    채용공고 삭제
    """

    queryset = JobPost.objects.all()


class JobPostReadView(ListAPIView):
    """
    채용공고 목록보기
    """

    serializer_class = JobPostSerializer
    queryset = JobPost.objects.all()
