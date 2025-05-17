#!/usr/bin/env bash
# exit on error
set -o errexit

# Python 환경 설정
echo "Installing dependencies..."
python -m pip install --upgrade pip

# 명시적으로 gunicorn 설치
pip install gunicorn

# 의존성 설치
pip install -r requirements.txt

# 설치된 패키지 확인
pip list

# 정적 파일 수집
python manage.py collectstatic --noinput

# 마이그레이션 적용
python manage.py migrate

# PATH 확인
echo "Current PATH: $PATH"
echo "Gunicorn location: $(which gunicorn || echo 'not found')"