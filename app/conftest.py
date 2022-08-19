import pytest
from mixer.backend.django import mixer
from apis.models import User, Company, JobPost


@pytest.fixture
def sample_user():
    return User.objects.create(
        name="test123",
        email="test123@example.com",
        is_company=False,
    )


@pytest.fixture
def sample_company_user():
    return User.objects.create(
        name="test1234",
        email="test1234@example.com",
        is_company=True,
    )


@pytest.fixture
def sample_company():
    return Company.objects.create(name="원티드", country="한국", region="서울")


@pytest.fixture
def sample_jobpost():
    company = mixer.blend(Company)
    user = mixer.blend(User, is_company=True)
    return JobPost.objects.create(
        title="백엔드 엔지니어 채용공고",
        content="백엔드 엔지니어 채용합니다",
        position="백엔드 엔지니어",
        compensation=1000000,
        skill="python",
        company=company,
        user=user,
    )
