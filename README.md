# .github

ttorok-app 조직의 공개 프로필과, 모든 레포에 적용되는 기본 템플릿.

**이 레포는 공개다.** 여기 있는 모든 파일을 누구나 볼 수 있다.

| 파일 | 역할 |
|---|---|
| `profile/README.md` | 조직 페이지(github.com/ttorok-app)에 보이는 공개 소개 |
| `profile/assets/banner-{light,dark}.svg` | 배너. `make_banner.py`로 생성 |
| `.github/pull_request_template.md` | PR 템플릿 (자체 템플릿이 없는 레포에 적용) |
| `.github/ISSUE_TEMPLATE/` | 이슈 템플릿: 버그, 기능, 결정 필요 |
| `CONTRIBUTING.md` | 기여 가이드 (모든 레포) |

멤버에게만 보이는 팀 페이지는 비공개 레포 `ttorok-app/.github-private`의 `profile/README.md`다.

조직 페이지는 **우리가 만드는 것**만 보여 준다. 브랜치 전략·온보딩·규칙 같은 개발 절차는 `CONTRIBUTING.md`와 ttorok-docs 하네스에 둔다.

## 공개 페이지에 넣지 않는 것

가격·판매 정책, 인프라·보안 구성, 내부 규칙·문서 내용, 비공개 레포 링크, 일정의 세부, 팀원 개인 정보. 출시 전 공개 범위는 서비스 소개다.

## 꾸미기

```bash
python3 profile/assets/make_banner.py    # 문구·색을 바꾼 뒤 배너 다시 생성
```

- 색은 ttorok-docs `09` 4절 디자인 토큰(오행 5색, `paper`, `ink`)만 쓴다.
- 이미지는 `profile/assets/`에 두고 상대 경로로 넣는다. 라이트·다크 두 벌은 `<picture>`로.
- 미리보기: 브랜치에 푸시한 뒤 그 브랜치의 `profile/README.md`를 GitHub에서 연다. 조직 페이지에는 `main`만 반영된다.
- 또록이 디자인이 확정되면 배너의 오행 원을 또록이 10종으로 바꾼다.
