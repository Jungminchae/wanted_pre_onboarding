from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    """
    공통 모델
    :created_at - 유저, 회사, 공고, 채용지원 등록일
    :updated_at - 유저, 회사, 공고, 채용지원 수정일
    """

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("등록일"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("수정일"))

    class Meta:
        abstract = True


class User(BaseModel):
    """
    유저 모델
    :이름 - 유저 이름
    :이메일 - 유저 이메일
    과제 요구사항에 따라 로그인과 같은 인증 절차가 없어 패스워드 생성하지 않음
    """

    name = models.CharField(max_length=255, verbose_name=_("이름"))
    email = models.EmailField(max_length=255, verbose_name=_("이메일"))
    is_company = models.BooleanField(verbose_name=_("기업회원여부"))

    class Meta:
        db_table = "users"


class Company(BaseModel):
    """
    회사 모델
    :name - 회사 이름
    :country - 회사의 국가
    :region - 회사의 지역
    """

    name = models.CharField(max_length=255, verbose_name=_("회사명"))
    country = models.CharField(max_length=255, verbose_name=_("국가"))
    region = models.CharField(max_length=255, verbose_name=_("지역"))

    class Meta:
        db_table = "companies"


class JobPost(BaseModel):
    """
    채용공고 모델
    :id - 채용공고 id, 채용공고의 특성상 매우 많은 수로 등록될 수 있어 BigAutoField로 설정
    :title - 채용공고 제목
    :content - 채용공고 내용
    :position - 채용직무
    :compensation - 채용보상금
    :skill - 채용 기술 스택
    :company - 채용 회사
    """

    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255, verbose_name=_("제목"))
    content = models.TextField(verbose_name=_("내용"))
    position = models.CharField(max_length=255, verbose_name=_("채용직무"))
    compensation = models.PositiveIntegerField(verbose_name=_("채용보상금"))
    skill = models.CharField(max_length=255, verbose_name=_("기술스택"))
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("작성자"))
    company = models.ForeignKey(
        "Company", on_delete=models.CASCADE, verbose_name=_("회사")
    )

    class Meta:
        db_table = "job_posts"


class Apply(BaseModel):
    """
    지원내역 모델
    :id - 지원내역 id, 지원내역의 특성상 매우 많은 수로 등록될 수 있어 BigAutoField로 설정
    :user - 지원자
    :job_post - 채용공고
    """

    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE)

    class Meta:
        db_table = "apply_lists"
        constraints = [
            models.UniqueConstraint(fields=["user", "job_post"], name="user_apply")
        ]
