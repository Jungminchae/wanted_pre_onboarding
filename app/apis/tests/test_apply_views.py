import pytest
from django.urls import reverse
from mixer.backend.django import mixer
from apis.models import JobPost, Apply


pytestmark = pytest.mark.django_db


def test_apply_jobpost_success(client, sample_user, sample_jobpost):
    """
    채용공고 지원 테스트 - 성공
    """
    url = reverse("apis:job_apply")
    user_id = sample_user.id
    jobpost_id = sample_jobpost.id

    data = {"user": user_id, "job_post": jobpost_id}
    response = client.post(data=data, path=url)
    assert response.status_code == 201


def test_apply_jobpost_fail_when_apply_twice(client, sample_user, sample_jobpost):
    """
    채용공고 지원 테스트 - 실패 (이미 지원한 채용공고에 지원할 수 없음)
    """
    url = reverse("apis:job_apply")
    user_id = sample_user.id
    jobpost_id = sample_jobpost.id

    data = {"user": user_id, "job_post": jobpost_id}
    response_1 = client.post(data=data, path=url)
    response_2 = client.post(data=data, path=url)

    assert response_1.status_code == 201
    assert response_2.status_code != 201


def test_apply_jobpost_success_when_apply_other_post(
    client, sample_user, sample_jobpost
):
    """
    채용공고 지원 테스트 - 성공 (다른 채용공고에 지원할 수 있음)
    """
    jobpost_2 = mixer.blend(JobPost)
    url = reverse("apis:job_apply")
    user_id = sample_user.id
    jobpost_id = sample_jobpost.id

    data_1 = {"user": user_id, "job_post": jobpost_id}
    data_2 = {"user": user_id, "job_post": jobpost_2.id}

    response_1 = client.post(data=data_1, path=url)
    response_2 = client.post(data=data_2, path=url)

    assert response_1.status_code == 201
    assert response_2.status_code == 201


def test_cancel_apply_jobpost_success(client, sample_user, sample_jobpost):
    """
    채용공고 지원 취소 테스트 - 성공
    """
    sample_apply = mixer.blend(Apply, user=sample_user, job_post=sample_jobpost)
    url = reverse("apis:job_apply_delete", kwargs={"pk": sample_apply.id})
    response = client.delete(path=url)
    assert response.status_code == 204
