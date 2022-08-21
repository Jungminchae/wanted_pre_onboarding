# 원티드 프리온보딩 백엔드 코스 선발 과제
​
## 사용 기술
-   Python 3.9
-   Postgresql 14
-   Django 4.0.6
-   Djangorestframework 3.13.1
-   Docker 20.10.16
-   Docker-compose 1.29.2

## 요구사항
-   채용공고 CRUD
    -   채용공고 등록, 수정, 삭제, 목록 불러오기, 상세보기, 검색  
    -   로그인 및 인증 시스템 생략  
        -   인증 시스템이 생략되어 유저 모델에는 password가 없음  
        
1.  **채용공고를 등록합니다.**
-   인증 시스템은 없지만 유저 테이블은 존재하고, 채용공고는 기업회원만 등록할 수 있도록 구현  
-   rest\_framework의 generic api view 중 CreateAPIView를 이용하여 구현  

2.  **채용공고를 수정합니다.**
-   채용공고 수정 역시 기업회원만 가능할 수 있도록 하였고, 추가로 작성자만 수정할 수 있도록 구현, 다만 body에 유저 아이디를 담아서 보내야 함(인증 시스템이 있다면 필요 없음)  
-   rest\_framework의 generic api view 중 UpdateAPIView를 이용하여 구현  
-   요구사항에 따라 회사 ID는 변경 불가능하도록 validation을 구현  

3.  **채용공고를 삭제합니다.**
-   rest\_framework의 generic api view 중 DestroyAPIView를 이용하여 구현  
-   작성자만 삭제할 수 있도록 해야 하나 인증시스템이 존재하지 않아 구현하지 못함 (**개선 필요**) 

4-1 **채용공고 목록을 가져옵니다.**
-   rest\_framework의 generic api view 중 ListAPIView를 이용하여 구현  

4-2. **채용공고 검색 기능 구현**
-   rest\_framework에 SearchFilter를 이용해서 채용공고 제목, 내용, 직무, 기술에서 키워드 검색이 되도록 구현  

5.  **채용 상세 페이지를 가져옵니다.**
-   채용 내용을 추가하여 상세하게 볼 수 있도록 구현(이거 해야됨)  
-   같은 회사에서 올린 다른 공고도 나타날 수 있도록 구현  
-   rest\_framework의 generic api view 중 RetrieveAPIView를 이용하여 구현  

6. **사용자는 채용공고에 지원합니다.**
-   rest\_framework의 generic api view 중 CreateAPIView를 이용하여 구현  
- 요구 사항에 맞게 같은 공고에 지원했던 지원자인지 validation을 하도록 구현했고 model 자체에도 제약조건을 걸어 같은 공고에 같은 지원자는 커밋이 안되도록 설정  

## 기타
-   pre-commit을 이용하여 코드 스타일을 flake8과 black을 따르게 함.  
-   pytest를 이용하여 간단한 unittest 구현  
-   컨테이너 기반의 개발을 진행. 아래 명령어로 test를 진행할 수 있음.  

```shell
docker-compose run --rm app sh -c "pytest"
```
