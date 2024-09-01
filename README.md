# MyBlog
<img src="myblog/static/README_images/myblog_main_page.PNG" width="100%"/>

<br>

## 목차

## 1. 프로젝트 목표

1. Django의 Class-Based Views를 활용하여 효율적이고 재사용 가능한 코드 구조 만들기
2. 사용자 친화적이고 반응형 디자인의 블로그 구축
3. 보안성과 확장성을 고려한 견고한 백엔드 시스템 개발
4. 사용자 경험을 개선하는 다양한 기능 구현

<br>

## 2. 주요 기능

### 1. 사용자 관리 (CustomUser 모델)

- 회원가입 및 로그인/로그아웃 기능
    - django-recaptcha를 사용한 로봇 방지 기능
    - dnspython을 활용한 이메일 유효성 검사
- 로그인/로그아웃 기능
- 프로필 페이지 (프로필 사진 및 자기소개 포함)
- 사용자 정보 수정 기능

### 2. 블로그 포스트 관리

- 포스트 작성, 수정, 삭제 기능
- 이미지 업로드 지원
- 카테고리 분류 시스템
- 조회수 집계

### 3. 댓글 시스템

- 포스트에 대한 댓글 작성 기능
- 답글(중첩 댓글) 기능
- 댓글 삭제 기능
- 소프트 삭제 구현 (is_deleted 필드 활용)

### 4. 좋아요 기능

- 포스트 및 댓글에 대한 좋아요 기능
- 사용자당 포스트 하나에 한 번만 좋아요 가능 (unique_together 제약조건)

### 5. 카테고리 관리

- 동적 슬러그 생성을 통한 검색 친화적 URL 구조(slugify)
- 카테고리별 포스트 목록 제공

### 6. 검색 및 필터링

- 포스트 제목, 내용, 작성자 기반 검색 기능
- 카테고리별 필터링 기능

### 7. 페이지네이션

- 포스트 목록에 대한 페이지네이션 구현

### 8. 권한 관리

- 관리자, 작성자, 일반 사용자 등 역할별 권한 설정
- 객체 레벨 권한 구현 (예: 자신의 포스트만 수정/삭제 가능)

이 프로젝트를 통해 Django의 강력한 CBV 기능들을 활용하며, 실제 운영 가능한 수준의 블로그 플랫폼을 개발하는 것이 최종 목표입니다.

<br>

# WBS

```mermaid
gantt
    title Django 블로그 프로젝트 개발 일정
    dateFormat  YYYY-MM-DD

    section 기획
    WBS 작성 :2024-08-26, 1d
    아이디어 기획 :2024-08-26, 2d
    와이어 프레임 작성 :2024-08-26, 2d
    ERD 작성 :2024-08-27, 1d

    section 개발
    URL 패턴 정의 :2024-08-27, 1d
    모델 설계 :2024-08-27, 1d
    CBV 구현 :2024-08-27, 2d
    CRUD 구현 :2024-08-28, 2d
    사용자 인증 :2024-08-29, 2d
    추가 기능 구현 :2024-08-29, 2d
    테스트 및 배포:2024-08-30, 1d

    section 문서 작성
    README 작성 :2024-08-30, 2d

    section 발표 준비
    발표 준비 :2024-09-01, 1d
```

<br>

# ERD
<img src="myblog/static/README_images/ERD.png" width="100%"/>


<br>

# 명세
| App      | URL Pattern                    | View                       | Description                     |
| -------- | ------------------------------ | -------------------------- | ------------------------------- |
| config   | /admin/                         | admin.site            | Django admin        |
| config   | /                        | MainPageView            | 메인페이지        |
| config   | blog/                        | blog url            | 블로그 url        |
| config   | accounts/                        | accounts url            | 계정 관련 url        |
| blog     | blog/                             | PostListView               | 블로그 게시물 목록              |
| blog     | blog/search/<str:tag>                        | PostSearchView                 | 제목, 내용, 글쓴이 중에 선택하여 검색               |
| blog     | blog/<int:id>                      | PostDetailView             | 블로그 게시물 상세              |
| blog     | blog/write                        | PostCreateView             | 블로그 게시물 생성              |
| blog     | blog/edit/<int:id>               | PostUpdateView             | 블로그 게시물 수정          |
| blog     | blog/delete/<int:id>               | PostDeleteView             | 블로그 게시물 삭제              |
| blog     | comment/<int:post_id>/add/               | CommentCreateView             | 게시물 댓글              |
| blog     | comment/<int:post_id>/<int:parent_id>/add/               | CommentCreateView               | 게시물 대댓글              |
| blog     | comment/<int:pk>/delete/               | CommentDeleteView              | 댓글 삭제              |
| accounts | accounts/login                      | CustomLoginView               | 사용자 로그인                     |
| accounts | accounts/logout                      | LogoutView               | 사용자 로그아웃                     |
| accounts | accounts/register/                      | SignUpView               | 사용자 등록                     |
| accounts | accounts/edit                      | UserProfileUpdateView               | 사용자 정보 수정                     |
| accounts | accounts/password_change                        | CustomPasswordChangeView            | 비밀번호 변경                   |

<br>

# 와이어 프레임 및 화면 설계 초안

[Figma URL](https://www.figma.com/design/teJ06xvveV1K8VuVuRbss0/Untitled?node-id=0-1&t=5dxv9WNU6DnQAgnH-0)

<table border="1" style="width:100%;">
  <colgroup>
    <col style="width: 50%;">
    <col style="width: 50%;">
  </colgroup>
    <tbody>
        <tr>
            <td>메인 페이지</td>
            <td>회원가입</td>
        </tr>
        <tr>
            <td>
		<img src="myblog/static/README_images/wf_main.png" width="100%"/>
            </td>
            <td>
                <img src="myblog/static/README_images/wf_register.png" width="100%"/>
            </td>
        </tr>
        <tr>
            <td>로그인</td>
            <td>게시글 리스트</td>
        </tr>
        <tr>
           <td>
                <img src="myblog/static/README_images/wf_login.png" width="100%"/>
            </td>
	     <td>
                <img src="myblog/static/README_images/wf_post_list.png" width="100%"/>
            </td>
        </tr>
        <tr>
            <td>게시글 리스트(로그인)</td>
            <td>프로필 수정</td>
        </tr>
        <tr>
            <td>
                <img src="myblog/static/README_images/wf_profile_post_list.png" width="100%"/>
            </td>
            <td>
                <img src="myblog/static/README_images/wf_profile.png" width="100%"/>
            </td>
        </tr>
        <tr>
            <td>새 게시글 작성</td>
            <td></td>
        </tr>
        <tr>
            <td>
                <img src="myblog/static/README_images/wf_post_form.png" width="100%"/>
            </td>
            <td>
            </td>
        </tr>
    </tbody>
</table>

<br>

# 화면 설계 및 구현 화면

