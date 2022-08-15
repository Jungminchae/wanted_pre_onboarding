import pytest 
from apis.models import User, Company, JobPost, ApplyList


pytestmark = pytest.mark.django_db


def test_user_model_success():
    '''
    유저 모델 테스트 - 성공
    '''    
    user = User.objects.create(
        name='test123',
        email="test123@example.com"
    )
    assert user.name == 'test123'
    assert user.email == "test123@example.com"

def test_company_model_success():
    '''
    회사 모델 테스트 - 성공
    '''    
    company = Company.objects.create(
        name='원티드',
        country='한국',
        region='서울'
    )
    assert company.name == '원티드'
    assert company.country == '한국'
    assert company.region == '서울'

def test_jobpost_model_success(sample_user, sample_company):
    '''
    채용공고 모델 테스트 - 성공
    '''    
    jobpost = JobPost.objects.create(
        title='백엔드 엔지니어 채용공고',
        content='백엔드 엔지니어 채용합니다',
        position='백엔드 엔지니어',
        compensation=1000000,
        skill='python',
        company=sample_company,
        user=sample_user
    )
    assert jobpost.title == '백엔드 엔지니어 채용공고'
    assert jobpost.content == '백엔드 엔지니어 채용합니다'
    assert jobpost.user == sample_user


def test_applylist_model_success(sample_user, sample_jobpost):
    '''
    지원 내역 모델 테스트 - 성공
    '''    
    applylist = ApplyList.objects.create(
        user=sample_user,
        job_post=sample_jobpost
    )
    assert applylist.user == sample_user
    assert applylist.job_post == sample_jobpost
