# 민요 플랫폼 (Minyo Platform)

민요 플랫폼은 한국 전통 민요를 배우고, 듣고, 녹음하고, 공유할 수 있는 웹 애플리케이션입니다.

## 주요 기능

- 다양한 지역의 민요 감상하기
- 전문가들의 민요 강의 듣기
- 직접 민요를 녹음하고 저장하기
- 커뮤니티에서 다른 사용자들과 소통하기

## 기술 스택

- **Backend**: Python, Django
- **Frontend**: HTML, CSS, JavaScript, Tailwind CSS
- **Database**: SQLite (개발), PostgreSQL (프로덕션)

## 설치 및 실행 방법

1. 프로젝트 클론:
   ```
   git clone https://github.com/yourusername/minyo-platform.git
   cd minyo-platform
   ```

2. 가상환경 생성 및 활성화:
   ```
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   # 또는
   venv\Scripts\activate  # Windows
   ```

3. 의존성 설치:
   ```
   pip install -r requirements.txt
   ```

4. Tailwind CSS 의존성 설치:
   ```
   npm install
   ```

5. Tailwind CSS 빌드:
   ```
   npm run build
   ```

6. 데이터베이스 마이그레이션:
   ```
   python manage.py migrate
   ```

7. 개발 서버 실행:
   ```
   python manage.py runserver
   ```

8. 브라우저에서 http://localhost:8000/ 접속

## 개발 모드

Tailwind CSS 변경사항을 자동으로 빌드하려면:
```
npm run watch
```

## 관리자 계정 생성

```
python manage.py createsuperuser
```

## 디렉토리 구조

- `accounts/`: 사용자 계정 관리
- `core/`: 공통 기능 및 기본 템플릿
- `minyo/`: 민요 듣기 기능
- `lessons/`: 강의 듣기 및 녹음 기능
- `community/`: 커뮤니티 기능
- `static/`: 정적 파일 (CSS, JS, 이미지)
- `media/`: 사용자 업로드 미디어 파일

## 기여하기

프로젝트에 기여하고 싶으시다면 이슈를 생성하거나 PR을 보내주세요. 