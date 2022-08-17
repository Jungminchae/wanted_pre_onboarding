import pytest
from django.urls import reverse
from mixer.backend.django import mixer
from apis.models import JobPost

pytestmark = pytest.mark.django_db


def test_jobpost_registration_success(client, sample_company_user, sample_company):
    """
    채용공고 등록 테스트 - 성공
    """
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


def test_jobpost_update_success(client, sample_jobpost):
    """
    채용공고 수정 테스트 - 성공
    """
    url = reverse("apis:jobpost_update", kwargs={"pk": sample_jobpost.id})
    data = {
        "title": "프론트 엔지니어 채용공고",
        "content": "프론트 엔지니어 채용합니다",
        "position": "프론트 엔지니어",
    }
    response = client.patch(data=data, path=url, content_type="application/json")
    assert response.status_code == 200


def test_jobpost_update_fail_when_fix_company_id(client, sample_jobpost):
    """
    채용공고 수정 테스트 - 실패 (채용공고의 회사 ID를 변경할 수 없음)
    """
    url = reverse("apis:jobpost_update", kwargs={"pk": sample_jobpost.id})
    data = {
        "title": "프론트 엔지니어 채용공고",
        "content": "프론트 엔지니어 채용합니다",
        "position": "프론트 엔지니어",
        "company": 2,
    }
    response = client.patch(data=data, path=url, content_type="application/json")
    assert response.status_code == 400


def test_jobpost_delete_success(client, sample_jobpost):
    """
    채용공고 삭제 테스트 - 성공
    """
    url = reverse("apis:jobpost_delete", kwargs={"pk": sample_jobpost.id})
    response = client.delete(path=url)
    assert response.status_code == 204


def test_jobpost_read_success(client):
    """
    채용공고 목록 보기 테스트 - 성공
    """
    mixer.cycle(20).blend(JobPost)
    url = reverse("apis:jobpost_read")
    response = client.get(path=url)
    assert response.status_code == 200
    assert len(response.json()) == 20
