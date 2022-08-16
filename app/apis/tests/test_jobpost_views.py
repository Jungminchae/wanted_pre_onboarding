import pytest
from django.urls import reverse

pytestmark = pytest.mark.django_db


def test_jobpost_registration_success(client, sample_company_user, sample_company):
    url = reverse("apis:jobpost_registration")
    user_id = sample_company_user.id
    company_id = sample_company.id
    data = {
        "title": "백엔드 엔지니어 채용공고",
        "content": "백엔드 엔지니어 채용합니다",
        "position": "백엔드 엔지니어",
        "compensation": 100000,
        "skill": "python",
        "user": user_id,
        "company": company_id,
    }
    response = client.post(data=data, path=url)
    assert response.status_code == 201
