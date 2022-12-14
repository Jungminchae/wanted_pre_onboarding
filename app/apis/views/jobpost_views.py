from rest_framework.generics import (
    CreateAPIView,
    UpdateAPIView,
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
)
from rest_framework.filters import SearchFilter
from apis.models import JobPost
from apis.serializers.jobpost_serializers import (
    JobPostSerializer,
    JobPostUpdateSerializer,
    JobPostRetrieveSerializer,
)
from apis.permissions import IsCompanyUser, IsOwner


class JobPostRegistrationView(CreateAPIView):
    """
    채용공고 등록
    """

    serializer_class = JobPostSerializer
    queryset = JobPost.objects.all()
    permission_classes = [IsCompanyUser]


class JobPostUpdateView(UpdateAPIView):
    """
    채용공고 수정
    :Company ID 제외, 전부 변경 가능
    """

    serializer_class = JobPostUpdateSerializer
    queryset = JobPost.objects.all()
    permission_classes = [IsCompanyUser, IsOwner]


class JobPostRetrieveView(RetrieveAPIView):
    """
    채용공고 상세 조회
    """

    serializer_class = JobPostRetrieveSerializer
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
    filter_backends = [SearchFilter]
    search_fields = ("title", "content", "position", "skill")
