import pytest
from django.urls import reverse
from mixer.backend.django import mixer
from apis.models import JobPost


pytestmark = pytest.mark.django_db


def test_apply_jobpost_success(client, sample_user, sample_jobpost):
    url = reverse("apis:job_apply")
    user_id = sample_user.id
    jobpost_id = sample_jobpost.id

    data = {"user": user_id, "job_post": jobpost_id}
    response = client.post(data=data, path=url)
    assert response.status_code == 201


def test_apply_jobpost_fail_when_apply_twice(client, sample_user, sample_jobpost):
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
